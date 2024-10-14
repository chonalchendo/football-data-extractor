import polars as pl
from functools import reduce
from typing import Iterator 

from .base import BasePlayerCrawler

from ..cleaners.common import common_cleaners

class PlayerDefense(BasePlayerCrawler):
    def __init__(self, season: str | None = None) -> None:
        print('Initializing PlayerDefense...')
        super().__init__(
            season=season,
            stat="defense",
            table="defense",
        )
        self.cleaners = common_cleaners

        print('PlayerDefense initialized.')

    def crawl(self) -> Iterator[dict]:  
        print('Crawling player defense data...')
        data = self.parse()
        data2 = reduce(
            lambda data, cleaner: cleaner(data), self.cleaners, data
        )
        data3 = data2.with_columns(
            pl.Series('season', [self.season] * len(data2)),
        )

        print(data3)

        for record in data3.to_dicts():
            yield record

if __name__ == "__main__":
    print("Crawling player defense data...")
    defense = PlayerDefense(season="2021-2022")
    print("Crawling...")
    for record in defense.crawl():
        print(record)
