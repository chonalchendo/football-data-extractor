from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class Foot(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        foots = [stat for stat in stats[5::8]]
        foots = [td.text if td.text else None for td in foots]
        return pl.Series(foots, name="foot")

