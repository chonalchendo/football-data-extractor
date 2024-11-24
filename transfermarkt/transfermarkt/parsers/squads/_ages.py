import polars as pl
from bs4 import BeautifulSoup

from ...config.parser_indexes import INDEXES


def parse_ages(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    pos = INDEXES[index]["ages"]
    stats = soup.find_all("td", {"class": "zentriert"})
    ages = [stat for stat in stats[pos::8]]
    dob = [td.text.strip().split(" (")[0] if td.text else None for td in ages]
    age = [
        int(td.text.strip().split(" (")[1].split(")")[0]) if td.text else None
        for td in ages
    ]
    return pl.DataFrame({"dob": dob, "age": age})
