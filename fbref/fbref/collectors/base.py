from collections.abc import Sequence
from typing import Iterator, Callable, TypeAlias 
from functools import reduce

import pandas as pd
import polars as pl

from pydantic import BaseModel 

from ..utils.logger import get_logger

logger = get_logger(__name__)


DataFrameTransform: TypeAlias = Callable[[pl.DataFrame], pl.DataFrame]


class BasePlayerCollector:
    def __init__(
        self,
        stat: str, 
        table: str, 
        validator: BaseModel,
        season: str | None = None,
        cleaners: Sequence[DataFrameTransform] = (),
    ) -> None:
        self.season = season
        self.stat = stat
        self.table = table
        self.validator = validator
        self.cleaners = cleaners
        self.url = "https://fbref.com/en/comps/Big5/{season}/{stat}/players/{season}-Big-5-European-Leagues-Stats#stats_{table}"

    def collect(self) -> Iterator[dict]:
        data = self.parse()
        data2 = reduce(lambda data, cleaner: cleaner(data), self.cleaners, data)
        data3 = data2.with_columns(
            pl.Series("season", [self.season] * len(data2)),
        )

        if data3.shape[0] == 0:
            logger.error(f"No data found for {self.stat} in {self.season}")
            raise ValueError

        print(data3.columns)

        for record in data3.to_dicts():
            valid_record = self.validator(**record)
            yield valid_record.model_dump()       


    def parse(self) -> pl.DataFrame:

        season = f"{self.season}-{str(int(self.season) + 1)}"
        logger.info(f"Collecting data for {season}")

        params = {"season": season, "stat": self.stat, "table": self.table}
        url = self.url.format(**params)

        logger.info(f"Collecting data from {url}")
        df_pandas = pd.read_html(url, skiprows=1, header=0)[0]
        return pl.from_pandas(df_pandas)

