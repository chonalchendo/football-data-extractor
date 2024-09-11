
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import polars as pl


class Parser(ABC):
    """ABC Protocol class for parsing data from transfermarkt."""

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame | pl.Series | tuple:
        pass
