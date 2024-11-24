import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_countries(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["countries"]
    stats = soup.find_all("td", {"class": "zentriert"})
    countries = [stat for stat in stats[pos::8]]
    countries = [
        td.find("img").get("title") if td.find("img") else None for td in countries
    ]
    return pl.DataFrame({"country": countries})
