from functools import reduce
from typing import Iterator

import polars as pl

from ..cleaners.common import common_cleaners
from ..cleaners.defense import defense_cleaners
from ..schemas import DefenseStats
from ..utils.logger import get_logger
from .base import BasePlayerCollector

logger = get_logger(__name__)


class PlayerDefense(BasePlayerCollector):
    def __init__(self, season: str | None = None) -> None:
        super().__init__(
            season=season,
            stat="defense",
            table="defense",
        )
        self.cleaners = common_cleaners + defense_cleaners

    def collect(self) -> Iterator[dict]:
        data = self.parse()
        data2 = reduce(lambda data, cleaner: cleaner(data), self.cleaners, data)
        data3 = data2.with_columns(
            pl.Series("season", [self.season] * len(data2)),
        )

        if data3.shape[0] == 0:
            logger.error(f"No data found for {self.stat} in {self.season}")
            raise ValueError

        for record in data3.to_dicts():
            valid_record = DefenseStats(**record)
            yield valid_record.model_dump()
