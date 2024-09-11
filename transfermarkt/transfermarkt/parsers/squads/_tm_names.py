from ..base import Parser
from bs4 import BeautifulSoup
import polars as pl


class TransfermarktName(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.Series:
        links = soup.find_all("td", {"class": "hauptlink"})
        tm_name = [
            link.find("a")["href"].split("/")[1] if link.find("a") else None
            for link in links[::2]
        ]
        return pl.Series(tm_name, name="tm_name")

