import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class Positions(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        pos_soup = soup.find_all("td", {"class": "posrela"})
        positions = [
            td.find_all("tr")[1].find("td").text.strip() if td.find_all("tr") else None
            for td in pos_soup
        ]
        return pl.DataFrame({"position": positions})
