from collections.abc import Sequence
from typing import Iterator

# from urllib.parse import urlparse

import polars as pl
import scrapy
from bs4 import BeautifulSoup
from pydantic import ValidationError
from scrapy.exceptions import CloseSpider
from scrapy.http import Response

from ..parsers.squads import squad_parsers
from ..schemas import Player
from ..parsers.base import Parser


class SquadsSpider(scrapy.Spider):
    name = "squads"
    allowed_domains = ["transfermarkt.co.uk"]
    url = (
        "https://transfermarkt.co.uk/{squad}/kader/verein/{id}/saison_id/{year}/plus/1"
    )

    def __init__(self, season: str | None = None, clubs: dict | None = None) -> None:
        self.season = season
        self.clubs = clubs
        self._parsers: Sequence[Parser] = squad_parsers
        self._parsed_squad_info: dict = {}

    def parse(self, response: Response) -> Iterator[dict]:
        """
        Parse the response and yield a dictionary with the squad data.

        @url https://transfermarkt.co.uk/arsenal-fc/kader/verein/11/saison_id/2020/plus/1
        @returns items 1
        @scrapes dob age country current_club foot height joined_date name number position signed_from signing_fee tm_squad_id tm_squad value season squad
        """
        soup = self.soupify(response)

        # concatenate parsers together
        data = pl.concat(
            [parser.parse(soup) for parser in self._parsers], how="horizontal"
        )

        # add season and squads to data
        # url = response.url
        # tm_squad = urlparse(url).path.split("/")[1]
        # season = int(urlparse(url).path.split("/")[6])

        # squad = get_squad_name(soup=soup)  # real squad name

        season = self._parsed_squad_info["season"]
        tm_squad_id = self._parsed_squad_info["tm_team_id"]
        tm_squad = self._parsed_squad_info["tm_team_name"]
        squad = self._parsed_squad_info["team_name"]

        data = data.with_columns(
            pl.Series("season", [season] * len(data)),
            pl.Series("tm_squad_id", [tm_squad_id] * len(data)),
            pl.Series("tm_squad", [tm_squad] * len(data)),
            pl.Series("squad", [squad] * len(data)),
        )

        for record in data.to_dicts():
            try:
                player = Player(**record)
                yield player.model_dump()
            except ValidationError as e:  # Pydantic error handling
                msg = f"Error parsing player: {record['name']}. Validation error: {e}"
                self.logger.error(msg)
                raise CloseSpider(msg)

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

        for row in self.clubs:
            for tm_team, id, tm_team in zip(
                row["tm_team_name"], row["tm_team_id"], row["team_name"]
            ):
                url = self.url.format(squad=tm_team, id=id, year=row["season"])

                # store values to add to final dataframe
                self._parsed_squad_info.update(
                    {
                        "tm_team_name": tm_team,
                        "tm_team_id": id,
                        "team_name": tm_team,
                        "season": row["season"],
                    }
                )

                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                )
