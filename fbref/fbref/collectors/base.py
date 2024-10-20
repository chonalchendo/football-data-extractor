from abc import ABC, abstractmethod
from typing import Iterator

import pandas as pd
import polars as pl

from ..utils.logger import get_logger

logger = get_logger(__name__)


class BasePlayerCollector(ABC):
    def __init__(
        self,
        season: str | None = None,
        stat: str | None = None,
        table: str | None = None,
    ) -> None:
        self.season = season
        self.stat = stat
        self.table = table
        self.url = "https://fbref.com/en/comps/Big5/{season}/{stat}/players/{season}-Big-5-European-Leagues-Stats#stats_{table}"

    @abstractmethod
    def collect(self) -> Iterator[dict]:
        pass

    def parse(self) -> pl.DataFrame:

        season = f"{self.season}-{str(int(self.season) + 1)}"
        logger.info(f"Collecting data for {season}")

        params = {"season": season, "stat": self.stat, "table": self.table}
        url = self.url.format(**params)

        logger.info(f"Collecting data from {url}")
        df_pandas = pd.read_html(url, skiprows=1, header=0)[0]
        return pl.from_pandas(df_pandas)
