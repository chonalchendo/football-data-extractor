import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class Countries(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        stats = soup.find_all("td", {"class": "zentriert"})
        countries = [stat for stat in stats[2::8]]
        countries = [
            td.find("img").get("title") if td.find("img") else None for td in countries
        ]
        return pl.DataFrame({"country": countries})
