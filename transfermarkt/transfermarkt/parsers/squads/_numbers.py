import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class Numbers(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        stats = soup.find_all("td", {"class": "zentriert"})
        numbers = [stat for stat in stats[0::8]]
        numbers = [
            (
                td.find("div", class_="rn_nummer").text.strip()
                if td.find("div", class_="rn_nummer")
                else None
            )
            for td in numbers
        ]
        return pl.DataFrame({"number": numbers})
