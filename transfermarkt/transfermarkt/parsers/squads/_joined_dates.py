import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class JoinedDate(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        stats = soup.find_all("td", {"class": "zentriert"})
        joined_date = [stat for stat in stats[6::8]]
        joined_date = [td.text if td.text else None for td in joined_date]
        return pl.DataFrame({"joined_date": joined_date})
