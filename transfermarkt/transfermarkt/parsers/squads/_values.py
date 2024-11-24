import polars as pl
from bs4 import BeautifulSoup


def parse_market_values(soup: BeautifulSoup) -> pl.DataFrame:
    values = soup.find_all("td", {"class": "rechts hauptlink"})
    values = [td.find("a").text if td.find("a") else "€0" for td in values]
    return pl.DataFrame({"value": values})
