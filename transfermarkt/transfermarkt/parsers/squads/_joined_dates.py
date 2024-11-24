import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_joined_date(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["joined_date"]
    stats = soup.find_all("td", {"class": "zentriert"})
    joined_date = [stat for stat in stats[pos::8]]
    joined_date = [td.text if td.text else None for td in joined_date]
    return pl.DataFrame({"joined_date": joined_date})
