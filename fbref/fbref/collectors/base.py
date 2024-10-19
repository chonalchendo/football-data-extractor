import pandas as pd
import polars as pl

from typing import Iterator
from abc import ABC, abstractmethod


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
        params = {
            'season': self.season,
            'stat': self.stat,
            'table': self.table
        }
        url = self.url.format(**params)
        df_pandas = pd.read_html(url, skiprows=1, header=0)[0]
        return pl.from_pandas(df_pandas)

