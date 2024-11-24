import polars as pl
from bs4 import BeautifulSoup

from transfermarkt.transfermarkt.config.parser_indexes import INDEXES


def parse_signing_info(soup: BeautifulSoup, index: str) -> pl.DataFrame:
    stats = soup.find_all("td", {"class": "zentriert"})
    pos = INDEXES[index]["signing_info"]
    signing_info = [stat for stat in stats[pos::8]]

    signed_from = [
        td.find("a").get("title").split(": Ablöse ")[0] if td.find("a") else None
        for td in signing_info
    ]
    signing_fee = [
        td.find("a").get("title").split(": Ablöse ")[1] if td.find("a") else "€0"
        for td in signing_info
    ]
    return pl.DataFrame({"signed_from": signed_from, "signing_fee": signing_fee})
