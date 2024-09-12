import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class CurrentClubs(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        current_clubs = [stat for stat in stats[3::8]]
        current_clubs = [
            td.find("a").get("title") if td.find("a") else None for td in current_clubs
        ]
        return pl.Series(current_clubs, name="current_club")
