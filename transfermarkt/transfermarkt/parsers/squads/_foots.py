import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_foot(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["foot"]
    stats = soup.find_all("td", {"class": "zentriert"})
    foots = [stat for stat in stats[pos::8]]
    foots = [td.text if td.text else None for td in foots]
    return pl.DataFrame({"foot": foots})
