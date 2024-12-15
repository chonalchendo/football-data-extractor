# Football Data Extractor

This project aims to provide the functionality to extract football data from various public resources and file to a users local project file system.
This project is the provides the code to extract data for the [Football Data Warehouse](https://github.com/chonalchendo/football-data-warehouse) project which aims to provide a comprehensive data warehouse for football data.

Currently, there is functionality to extract data from two sources:

- [Fbref](https://fbref.com/en/)
  - Player related stats such as shooting, passing, and defense.
  - Also provides data on player wages.
- [Transfermarkt](https://www.transfermarkt.co.uk/)
  - Player market valuation data and general player information.

In future, more sources will be added.

## Setup

If you would like to use this project independently of [Football Data Warehouse](https://github.com/chonalchendo/football-data-warehouse), you can follow the steps below to set up the project.

The package manager used for this project is [uv](https://docs.astral.sh/uv/).

1. Clone the repository

```bash
git clone
```

2. Install `uv` for package management

```bash
pip install uv
```

3. Create a virtual environment and specify the python version to use

```bash
uv venv --python 3.12
```

4. Install the required packages by running `uv install`

```bash
uv sync
```

4. Activate the uv virtual environment if not already activated

```bash
source .venv/bin/activate
```

## Usage

To use the code in this project, you can define each directory as a dependency within your own project.
To do this, you don't need to follow the virtual environment instructions above.

For example, the two main directories are `fbref` and `transfermarkt`. You can install these as dependencies using `uv` in another repo like I have done
in the [Football Data Warehouse](https://github.com/chonalchendo/football-data-warehouse) project.

```bash
uv add https://github.com/chonalchendo/football-data-extractor.git
```

This will then allow you to use the `fbref` and `transfermarkt` packages inside your own project.

### Fbref example

Fbref is a custom extractor developed using `pandas` and `beautifulsoup` to extract data from the fbref website.

```python

from fbref import fbref

from .settings import get_config


def run_stats_crawler(collector: str, season: str) -> None:
    settings = get_config().fbref_extract
    feed = fbref.ParquetFeed(
        output_path=settings.FEEDS.PATH,
        format=settings.FEEDS.FORMAT,
    )
    runner = fbref.NavigatorRunner(feed=feed)
    runner.navigate(collector=collector, season=season)
    runner.start()
```

### Transfermarkt example

Transfermarkt is built using `scrapy` to extract data from the transfermarkt website.

```python
from pathlib import Path

import polars as pl
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

from .settings import get_config


def set_scrapy_settings() -> Settings:
    settings = get_project_settings()
    config = get_config()

    scrapy_settings = config.transfermarkt_extract.model_dump(exclude=None)

    settings.setdict(scrapy_settings)
    return settings

def run_squads_spider(crawler: str, season: str) -> None:
    settings = set_scrapy_settings()
    process = CrawlerProcess(settings)

    clubs_path = Path(f"data/raw/transfermarkt/{season}/clubs.parquet").resolve()
    clubs_df = pl.read_parquet(clubs_path, use_pyarrow=True)

    clubs = clubs_df.to_dicts()

    process.crawl(crawler, season=season, clubs=clubs)
    process.start()

```

Beacause it is built using `scrapy`, you can run the spider using the `CrawlerProcess` class by passing the spider information.

In the above example, I load in my spider settings from a pydantic settings model in the same way you do in a `scrapy` project via the `settings.py` file.

```python
from typing import Any

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TransfermarktConfig(BaseSettings):
    SPIDER_MODULES: list[str] = ["transfermarkt"]
    NEWSPIDER_MODULE: list[str] = ["transfermarkt"]
    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )
    ROBOTSTXT_OBEY: bool = True
    DOWNLOAD_DELAY: int = 1
    COOKIES_ENABLED: bool = False
    REQUEST_FINGERPRINTER_IMPLEMENTATION: str = "2.7"
    TWISTED_REACTOR: str = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    FEED_EXPORT_ENCODING: str = "utf-8"
    ITEM_PIPELINES: dict[str, int] = Field(
        default_factory=lambda: {
            "transfermarkt.transfermarkt.pipelines.TransfermarktParquetPipeline": 300
        }
    )
    FEEDS: dict[str, Any] = Field(
        default_factory=lambda: {
            "data/raw/transfermarkt/{season}/{name}.parquet": {"format": "parquet"}
        }
    )
   )
```

Returning the above as a dictionary and passing it to the `CrawlerProcess` lets scrapy know what scraper to use and where to save the data.

## Future Work

- Add more sources to extract data from.
- Add more datasets from existing sources.

These goals will happen at some point in the future. If you would like to contribute to this project, please feel free to open a PR.
