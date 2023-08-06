import os
import shutil
import binascii
import sqlite3
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import PathLike
from pathlib import Path
from typing import Dict, Tuple

import pandas as pd
from tqdm import tqdm

from dicomselect.query import Query
from dicomselect.queryfactory import QueryFactory
from dicomselect.reader import DICOMImageReader


class Database:
    def __init__(self, db_path: PathLike):
        self._db_path = Path(db_path).absolute()
        self._errors = []
        self._conn = None
        self._query_factory = None

    def __enter__(self) -> Query:
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self) -> Query:
        with open(self._db_path, "rb") as f:
            file_header = binascii.hexlify(f.read(16)).decode("utf-8")
        # official sqlite3 file header
        if not file_header.startswith("53514c69746520666f726d6174203300"):
            sqlite3.DatabaseError(f'{self._db_path} does not appear to be a valid database')

        self._conn = sqlite3.connect(self._db_path)
        self._query_factory = QueryFactory(self._conn)
        return self._query_factory.create_query(None)

    def close(self):
        self._conn.close()

    def create(self, data_dir: PathLike, max_workers: int = 4, *additional_dicom_tags: str):
        """Build a database from DICOMs in subdirectories of data_dir.

        Parameters
        ----------
        data_dir
        max_workers
        additional_dicom_tags
        """
        self._errors = []

        data_dir = Path(data_dir).absolute()
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temp_dir:
            temp_db = Path(temp_dir) / 'temp.db'
            subdirectories = [data_dir / path for path in os.listdir(data_dir)]

            example_metadata = None
            for subdir in subdirectories:
                try:
                    root, _ = next(self._dicoms_in_dir(subdir))
                    reader = DICOMImageReader(root, allow_raw_tags=False, *additional_dicom_tags)
                    example_metadata = reader.metadata
                    columns = ', '.join(sorted([f'{name} {dtype}' for name, dtype in reader.column_info().items()]))
                    break
                except StopIteration:
                    pass
            if example_metadata is None:
                raise sqlite3.DataError(f'No dicom data found in {data_dir}')

            cursor = sqlite3.connect(temp_db)
            cursor.execute(f'CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, series_length INTEGER, path TEXT, {columns});')
            cursor.close()

            print(f"Creating database from DICOMs subdirectories of {data_dir}. Collecting all subdirectories...")

            subdirectories = [data_dir / path for path in os.listdir(data_dir)]
            with tqdm(total=len(subdirectories)) as pbar, ThreadPoolExecutor(max_workers=max_workers) as pool:
                futures = [pool.submit(self._thread_execute_dir, temp_db, path.absolute(), additional_dicom_tags) for path in subdirectories]
                for future in as_completed(futures):
                    self._errors.append(future.exception())
                    pbar.update()

            cursor = sqlite3.connect(temp_db, timeout=10)
            df_meta = pd.DataFrame({'DataDirectory': str(data_dir)}, index=[0])
            df_meta.to_sql(name='meta', con=cursor, if_exists='replace')
            cursor.close()

            if self._db_path.exists():
                os.remove(self._db_path)
            shutil.copy(temp_db, self._db_path)

            self._errors = [err for err in self._errors if err]
            print(f"Database created at {self._db_path} with {len(self._errors)} errors.")
            for e in self._errors:
                if e:
                    print('\t' + str(e))

    def _dicoms_in_dir(self, subdir: Path) -> Tuple[Path, Path]:
        for root, _, filenames in os.walk(subdir, onerror=lambda err: self._errors.append(err)):
            if any([file.endswith('.dcm') for file in filenames]) or 'dicom.zip' in filenames:
                rel_path = Path(root).relative_to(subdir.parent)
                yield root, rel_path

    def _metadata_in_dir(self, subdir: Path, *additional_tags: str):
        for root, rel_path in self._dicoms_in_dir(subdir):
            metadata = dict()
            try:
                reader = DICOMImageReader(root, allow_raw_tags=False, *additional_tags)
                metadata = reader.metadata
                metadata["series_length"] = len(reader.dicom_slice_paths)
                metadata["path"] = str(rel_path)
            except BaseException as e:
                self._errors.append(str(e))
            if metadata:
                yield metadata

    def _thread_execute_dir(self, db: Path, subdir: Path, additional_tags: Dict[str, str]):
        with sqlite3.connect(db, timeout=10, check_same_thread=False) as conn:
            df_rows = pd.DataFrame.from_dict(list(self._metadata_in_dir(subdir, additional_tags)), orient='columns')
            df_rows.to_sql(name='data', con=conn, if_exists='append', index=False)
