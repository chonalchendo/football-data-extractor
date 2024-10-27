from collections.abc import Sequence
from pathlib import Path

import polars as pl

from .utils.logger import get_logger

logger = get_logger(__name__)


class NdjsonFeedWriter:
    """
    A simple writer that streams dictionary data to a Parquet file.
    Similar to Scrapy's Feed exports but for Parquet format.
    """

    def __init__(self, output_path: str, format: str, overwrite: bool = False) -> None:
        self.output_path = Path(output_path)
        self.items: Sequence[dict] = []
        self.format = format
        self.overwrite = overwrite

        if not Path(self.output_path).parent.exists():
            logger.info(f"Creating directory {Path(self.output_path).parent}")
            Path(self.output_path).parent.mkdir(parents=True, exist_ok=True)

        # if mode is append, check if file exists
        if self.overwrite == "a" and not self.output_path.exists():
            self.overwrite = "w"

    def write(self, item: dict) -> None:
        """Write a single item (dictionary) to the feed"""
        self.items.append(item)

    def close(self) -> None:
        """Close the feed and write all items to Parquet"""
        if self.items:
            if not self.overwrite and self.output_path.exists():
                self._update_file()

            if self.overwrite:
                self._new_file()

    def _update_file(self) -> None:
        """Update an existing file with new items"""

        if self.format == "parquet" and ".parquet" in self.output_path:
            df = pl.read_parquet(self.output_path)
            df = df.extend(pl.DataFrame(self.items))
            df.write_parquet(self.output_path)

        if self.format == "ndjson" and ".ndjson" in self.output_path:
            df = pl.read_ndjson(self.output_path)
            df = df.extend(pl.DataFrame(self.items))
            df.write_ndjson(self.output_path)

    def _new_file(self) -> None:
        """Create a new file and write items to it"""
        if self.format == "parquet":
            df = pl.DataFrame(self.items)
            df.write_parquet(self.output_path)

        if self.format == "ndjson":
            df = pl.DataFrame(self.items)
            df.write_ndjson(self.output_path)
