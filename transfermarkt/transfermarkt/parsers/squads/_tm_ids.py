import polars as pl
from bs4 import BeautifulSoup

from ..base import Parser


class TransfermarktId(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        links = soup.find_all("td", {"class": "hauptlink"})
        tm_id = [
            link.find("a")["href"].split("/")[4] if link.find("a") else None
            for link in links[::2]
        ]
        return pl.Series(tm_id, name="tm_id")
