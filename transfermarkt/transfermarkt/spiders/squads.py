import polars as pl
import scrapy
from bs4 import BeautifulSoup
from rich import print

from ..parsers.squads import squad_parsers


class SquadsSpider(scrapy.Spider):
    name = "squads"
    allowed_domains = ["transfermarkt.co.uk"]
    url = (
        "https://transfermarkt.co.uk/{squad}/kader/verein/{id}/saison_id/{year}/plus/1"
    )

    def __init__(self, squad, id, year):
        self.squad = squad
        self.id = id
        self.year = year
        self.parsers = squad_parsers

    def parse(self, response):
        soup = self.soupify(response)

        data = pl.concat([parser.parse(soup) for parser in self.parsers])

        print(data)

        yield data.to_dicts()

    def soupify(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def start_requests(self):

        for squad, id, year in zip(self.squad, self.id, self.year):
            url = self.url.format(squad=squad, id=id, year=year)

            yield scrapy.Request(
                url=url,
                callback=self.parse,
            )
