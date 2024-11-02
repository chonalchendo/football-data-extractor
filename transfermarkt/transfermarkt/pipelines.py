from typing import Any
import polars as pl
import gcsfs
from scrapy import Spider
from scrapy.crawler import Crawler


class TransfermarktPolarsPipeline:
    def __init__(self) -> None:
        self.data = []

    def process_item(self, item, spider):
        self.data.append(item)
        return item

    def close_spider(self, spider) -> pl.DataFrame:
        df = pl.DataFrame(self.data)
        return df


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
            taken=self.credentials_path,
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

        feeds = spider.settings.getdict("FEEDS").keys()[0]

        with self.fs.open(feeds, mode="wb") as f:
            data.write_parquet(f, use_pyarrow=True)
