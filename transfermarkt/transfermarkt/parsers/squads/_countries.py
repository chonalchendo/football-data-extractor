from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class Countries(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        stats = soup.find_all("td", {"class": "zentriert"})
        countries = [stat for stat in stats[2::8]]
        countries = [
            td.find("img").get("title") if td.find("img") else None for td in countries
        ]
        return pl.Series(countries, name="country")

