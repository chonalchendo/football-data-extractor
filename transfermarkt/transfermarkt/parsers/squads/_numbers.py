import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_numbers(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["numbers"]
    stats = soup.find_all("td", {"class": "zentriert"})
    numbers = [stat for stat in stats[pos::8]]
    numbers = [
        (
            td.find("div", class_="rn_nummer").text.strip()
            if td.find("div", class_="rn_nummer")
            else None
        )
        for td in numbers
    ]
    return pl.DataFrame({"number": numbers})
