from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class Heights(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        heights = [stat for stat in stats[4::8]]
        heights = [td.text if td.text else None for td in heights]
        return pl.Series(heights, name="height")

