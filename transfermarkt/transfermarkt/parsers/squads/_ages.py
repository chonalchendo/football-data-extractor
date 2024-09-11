from bs4 import BeautifulSoup
import polars as pl

from ..base import Parser


class Ages(Parser):
    def parse(self, soup: BeautifulSoup) -> pl.DataFrame:
        stats = soup.find_all("td", {"class": "zentriert"})
        ages = [stat for stat in stats[1::8]]
        dob = [td.text.strip().split(" (")[0] if td.text else None for td in ages]
        age = [
            int(td.text.strip().split(" (")[1].split(")")[0]) if td.text else None
            for td in ages
        ]
        return pl.DataFrame({"dob": dob, "age": age})
