import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_current_club(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["current_club"]
    stats = soup.find_all("td", {"class": "zentriert"})
    current_clubs = [stat for stat in stats[pos::8]]
    current_clubs = [
        td.find("a").get("title") if td.find("a") else None for td in current_clubs
    ]
    return pl.DataFrame({"current_club": current_clubs})
