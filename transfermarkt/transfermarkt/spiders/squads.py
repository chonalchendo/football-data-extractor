from typing import Iterator
from urllib.parse import urlparse

import polars as pl
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Response

from ..parsers.squads import squad_parsers


class SquadsSpider(scrapy.Spider):
    name = "squads"
    allowed_domains = ["transfermarkt.co.uk"]
    url = (
        "https://transfermarkt.co.uk/{squad}/kader/verein/{id}/saison_id/{year}/plus/1"
    )

    def __init__(self, season=None) -> None:
        self.season = season
        self.parsers = squad_parsers

    def parse(self, response: Response) -> Iterator[dict]:
        """
        Parse the response and yield a dictionary with the squad data.

        @url https://transfermarkt.co.uk/arsenal-fc/kader/verein/11/saison_id/2020/plus/1
        @returns items 1
        @scrapes dob age country current_club foot height joined_date name number position signed_from signing_fee tm_id tm_name value season squad
        """
        soup = self.soupify(response)

        # concatenate parsers together
        data = pl.concat(
            [parser.parse(soup) for parser in self.parsers], how="horizontal"
        )

        # add season and squads to data
        url = response.url
        squad = urlparse(url).path.split("/")[1]
        season = urlparse(url).path.split("/")[6]

        data = data.with_columns(
            pl.Series("season", [season] * len(data)),
            pl.Series("squad", [squad] * len(data)),
        )

        for record in data.to_dicts():
            yield record

    def soupify(self, response: Response) -> BeautifulSoup:
        """
        Convert the response to a BeautifulSoup object.
        """
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def start_requests(self) -> Iterator[scrapy.Request]:
        """
        Starts the request for the given squads and seasons.
        @return request 1
        """

        path = "data/clubs.json.gz"
        clubs = pl.read_ndjson(path).sort("season")

        # filter based on the season
        match self.season:
            case "all":
                pass
            case None:
                raise ValueError("No season provided")
            case _:
                clubs = clubs.filter(pl.col("season") == str(self.season))

        for row in clubs.to_dicts():
            for team, id in zip(row["team_name"], row["team_id"]):
                url = self.url.format(squad=team, id=id, year=row["season"])
                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                )
