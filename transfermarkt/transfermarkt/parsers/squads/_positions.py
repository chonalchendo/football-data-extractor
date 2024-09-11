from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class Positions(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        pos_soup = soup.find_all("td", {"class": "posrela"})
        positions = [
            td.find_all("tr")[1].find("td").text.strip() if td.find_all("tr") else None
            for td in pos_soup
        ]
        return pl.Series(positions, name="position")

