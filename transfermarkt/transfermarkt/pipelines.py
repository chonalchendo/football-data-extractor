from pathlib import Path
from typing import Any

import gcsfs
import polars as pl
from scrapy import Spider
from scrapy.crawler import Crawler


class TransfermarktGCSPipeline:
    def __init__(self, gcp_project_name: str, credentials_path: str) -> None:
        self.data: list[dict[str, Any]] = []
        self.gcp_project_name: str = gcp_project_name
        self.credentials_path: str = credentials_path

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> "TransfermarktGCSPipeline":
        """
        Creates pipeline instance with settings from crawler.
        This method is called by Scrapy when creating the pipeline.
        """
        return cls(
            gcp_project_name=crawler.settings.get("GCP_PROJECT"),
            credentials_path=crawler.settings.get("GCP_CREDENTIALS_PATH"),
        )

    def open_spider(self, spider: Spider) -> None:
        self.fs = gcsfs.GCSFileSystem(
            project=self.gcp_project_name,
            token=self.credentials_path,
        )

    def process_item(self, item: dict[str, Any], spider: Spider) -> None:
        self.data.append(item)
        return item

    def close_spider(self, spider: Spider) -> None:
        data = (
            pl.DataFrame(self.data)
            if (len(self.data) > 0)
            else ValueError("DataFrame is Empty")
        )

        feeds: str = list(spider.settings.getdict("GCS_FEEDS").keys())[0]
        formatted_feeds = feeds.format(season=spider.season, name=spider.name)

        with self.fs.open(formatted_feeds, mode="wb") as f:
            data.write_parquet(f, use_pyarrow=True)


class TransfermarktParquetPipeline:
    def __init__(self) -> None:
        self.data: list[dict[str, Any]] = []

    def process_item(self, item: dict[str, Any], spider: Spider) -> None:
        self.data.append(item)
        return item

    def close_spider(self, spider: Spider) -> None:
        data = (
            pl.DataFrame(self.data)
            if (len(self.data) > 0)
            else ValueError("DataFrame is Empty")
        )

        feeds: str = list(spider.settings.getdict("FEEDS").keys())[0]
        formatted_feeds = feeds.format(season=spider.season, name=spider.name)

        Path(formatted_feeds).parent.mkdir(parents=True, exist_ok=True)

        data.write_parquet(formatted_feeds, use_pyarrow=True)


class TransfermarktDataFramePipeline:
    def __init__(self) -> None:
        self.data: list[dict[str, Any]] = []

    def process_item(self, item: dict[str, Any], spider: Spider) -> None:
        self.data.append(item)
        return item

    def close_spider(self, spider: Spider) -> pl.DataFrame:
        if len(self.data) == 0:
            raise ValueError("DataFrame is Empty")

        return pl.DataFrame(self.data)
