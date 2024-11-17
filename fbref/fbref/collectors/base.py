from collections.abc import Sequence
from functools import reduce
from typing import Callable, Iterator, TypeAlias, TypedDict

import pandas as pd
import polars as pl
from pydantic import BaseModel

from ..utils.logger import get_logger

logger = get_logger(__name__)


DataFrameTransform: TypeAlias = Callable[[pl.DataFrame], pl.DataFrame]


class Params(TypedDict):
    season: str | None = None


class StatsParams(Params):
    stat: str
    table: str


class WageParams(Params):
    comp_id: str
    comp_name: str


class BasePlayerCollector:
    def __init__(
        self,
        validator: BaseModel,
        url: str,
        url_params: Params,
        season: str | None = None,  # set later
        cleaners: Sequence[DataFrameTransform] = (),
    ) -> None:
        self.season = season
        self.validator = validator
        self.cleaners = cleaners
        self.url_params = url_params
        self.url = url

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
            valid_record: BaseModel = self.validator(**record)
            yield valid_record.model_dump()

    def parse(self) -> pl.DataFrame:

        season = f"{self.season}-{str(int(self.season) + 1)}"
        logger.info(f"Collecting data for {season}")

        self.url_params["season"] = season

        url = self.url.format(**self.url_params)

        logger.info(f"Collecting data from {url}")
        
        if 'wages' in url:
            df_pandas = pd.read_html(url)[1]
            return pl.from_pandas(df_pandas)
        
        df_pandas = pd.read_html(url, skiprows=1, header=0)[0]
        return pl.from_pandas(df_pandas)
