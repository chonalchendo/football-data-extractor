from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class Names(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        elements = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
        names = [td.get("title") if td.get("title") else None for td in elements]
        return pl.Series(names, name="name")

