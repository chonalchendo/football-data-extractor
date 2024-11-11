from abc import ABC, abstractmethod
from typing import Any

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
    def write(self, item: dict[str, Any]) -> None:
        pass

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
            project=self.gcs_project_name, token=self.gcs_credentials
        )

    def write(self, item: dict) -> None:
        self.items.append(item)

    def close(self) -> None:
        if not self.items:
            logger.error("No items to write - DataFrame would be empty")

        try:
            data = pl.DataFrame(self.items)

            with self.fs.open(self.output_path, mode="wb") as f:
                data.write_parquet(f, use_pyarrow=True)
                logger.info(
                    f"Successfully wrote {len(self.items)} items to {self.output_path}"
                )
        except Exception as e:
            logger.error(f"Failed to write data to {self.output_path}: {str(e)}")
            raise

class ParquetFeed(Feed):
    def __init__(self, output_path: str, format: str) -> None:
        super().__init__(output_path, format)

    def write(self, item: dict) -> None:
        self.items.append(item)

    def close(self) -> None:
        if not self.items:
            logger.error("No items to write - DataFrame would be empty")

        try:
            data = pl.DataFrame(self.items)
            data.write_parquet(self.output_path, use_pyarrow=True)
            logger.info(
                f"Successfully wrote {len(self.items)} items to {self.output_path}"
            )
        except Exception as e:
            logger.error(f"Failed to write data to {self.output_path}: {str(e)}")
            raise
