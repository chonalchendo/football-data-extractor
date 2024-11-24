import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_heights(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["height"]
    stats = soup.find_all("td", {"class": "zentriert"})
    heights = [stat for stat in stats[pos::8]]
    heights = [td.text if td.text else None for td in heights]
    return pl.DataFrame({"height": heights})
