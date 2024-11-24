import polars as pl
from bs4 import BeautifulSoup


def parse_names(soup: BeautifulSoup) -> pl.DataFrame:
    elements = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    names = [td.get("title") if td.get("title") else None for td in elements]
    return pl.DataFrame({"name": names})
