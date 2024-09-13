import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class Heights(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        stats = soup.find_all("td", {"class": "zentriert"})
        heights = [stat for stat in stats[4::8]]
        heights = [td.text if td.text else None for td in heights]
        return pl.DataFrame({"height": heights})
