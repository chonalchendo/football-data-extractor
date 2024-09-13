import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class Values(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        values = soup.find_all("td", {"class": "rechts hauptlink"})
        values = [td.find("a").text if td.find("a") else "€0" for td in values]
        return pl.DataFrame({"value": values})
