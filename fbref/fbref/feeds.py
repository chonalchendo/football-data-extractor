from abc import ABC, abstractmethod
from pathlib import Path

import gcsfs
import polars as pl

from .utils.logger import get_logger

logger = get_logger(__name__)


class Feed(ABC):
    def __init__(self, output_path: str, format: str) -> None:
        self.output_path = output_path
        self.format = format
        self.items: list[dict] = []

    @abstractmethod
    def write(self, item: dict) -> None:
        self.items.append(item)

    @abstractmethod
    def close(self) -> None:
        pass


class GcsFeed(Feed):
    def __init__(
        self, output_path: str, format: str, gcs_project_name: str, gcs_credentials: str
    ) -> None:
        super().__init__(output_path, format)
        self.gcs_project_name = gcs_project_name
        self.gcs_credentials = gcs_credentials
        self.fs = gcsfs.GCSFileSystem(
            project=self.gcs_project_name,
            token=self.gcs_credentials
        )

    def close(self) -> None:
        data = (
            pl.DataFrame(self.items)
            if (len(self.items) > 0)
            else ValueError("DataFrame is Empty")
        )

        with self.fs.open(self.output_path, mode="wb") as f:
            data.write_parquet(f, use_pyarrow=True)


# class ParquetFeedWriter:
#     """
#     A simple writer that streams dictionary data to a Parquet file.
#     Similar to Scrapy's Feed exports but for Parquet format.
#     """

#     def __init__(
#         self,
#         output_path: str,
#         format: str,
#         overwrite: bool = False,
#         gcs_project_name: str | None = None,
#         gcs_credentials: str | None = None,
#     ) -> None:
#         self.output_path = Path(output_path)
#         self.items: list[dict] = []
#         self.format = format
#         self.overwrite = overwrite
#         self.gcs_project_name = gcs_project_name
#         self.gcs_credentials = gcs_credentials
#         self.fs = (
#             gcsfs.GCSFileSystem(
#                 project=self.gcs_project_name,
#                 token=self.gcs_credentials,
#             )
#             if self.gcs_project_name is not None and self.gcs_credentials is not None
#             else None
#         )

#         if not Path(self.output_path).parent.exists():
#             logger.info(f"Creating directory {Path(self.output_path).parent}")
#             Path(self.output_path).parent.mkdir(parents=True, exist_ok=True)

#         # if mode is append, check if file exists
#         if self.overwrite == "a" and not self.output_path.exists():
#             self.overwrite = "w"

#     def write(self, item: dict) -> None:
#         """Write a single item (dictionary) to the feed"""
#         self.items.append(item)

#     def close(self) -> None:
#         """Close the feed and write all items to Parquet"""
#         if self.items:
#             if not self.overwrite and self.output_path.exists():
#                 self._update_file()

#             if self.overwrite:
#                 self._new_file()

#     def _update_file(self) -> None:
#         """Update an existing file with new items"""

#         if self.format == "parquet" and ".parquet" in self.output_path:
#             df = pl.read_parquet(self.output_path)
#             df = df.extend(pl.DataFrame(self.items))
#             df.write_parquet(self.output_path)

#     def _new_file(self) -> None:
#         """Create a new file and write items to it"""
#         if self.format == "parquet":
#             df = pl.DataFrame(self.items)
#             df.write_parquet(self.output_path)


# class GcsFeedWriter:
#     def __init__(self) -> None:
#         pass

#     def _write_to_gcs(self) -> None:
#         data = (
#             pl.DataFrame(self.items)
#             if (len(self.items) > 0)
#             else ValueError("DataFrame is Empty")
#         )

#         with self.fs.open(self.output_path, mode="wb") as f:
#             data.write_parquet(f, use_pyarrow=True)
