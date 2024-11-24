import polars as pl
from bs4 import BeautifulSoup


def parse_transfermarkt_name(soup: BeautifulSoup) -> pl.DataFrame:
    links = soup.find_all("td", {"class": "hauptlink"})
    tm_name = [
        link.find("a")["href"].split("/")[1] if link.find("a") else None
        for link in links[::2]
    ]
    return pl.DataFrame({"tm_name": tm_name})
