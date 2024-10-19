import polars as pl
from functools import reduce
from typing import Iterator 
import gzip
import json
from pathlib import Path

from .base import BasePlayerCollector

from ..cleaners.common import common_cleaners
from ..cleaners.defense import defense_cleaners 
from ..schemas import DefenseStats


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
        data2 = reduce(
            lambda data, cleaner: cleaner(data), self.cleaners, data
        )
        data3 = data2.with_columns(
            pl.Series('season', [self.season] * len(data2)),
        )


        for record in data3.to_dicts():
            valid_record = DefenseStats(**record)
            yield valid_record.model_dump()

if __name__ == "__main__":

    filepath = "fbref/data/defense/2021-2022/defense.json.gz"

    print(Path(__file__).resolve())

    if not Path(filepath).parent.exists():
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

    defense = PlayerDefense(season="2021-2022")
    for i, record in enumerate(defense.collect()):

        if i == 0:
            file = gzip.open(filepath, "wt")
            file.write(json.dumps(record))

        else:
            file = gzip.open(filepath, "at")
            file.write("\n")
            file.write(json.dumps(record))

    print("Done")

