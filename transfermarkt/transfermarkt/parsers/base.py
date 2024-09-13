from abc import ABC, abstractmethod

import polars as pl
from bs4 import BeautifulSoup


class Parser(ABC):
    """ABC Protocol class for parsing data from transfermarkt."""

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        pass
