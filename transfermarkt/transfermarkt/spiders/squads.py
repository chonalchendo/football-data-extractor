from typing import Iterator

import polars as pl
import scrapy
from bs4 import BeautifulSoup
from pydantic import ValidationError
from scrapy.exceptions import CloseSpider
from scrapy.http import Response

from ..parsers.squads import get_squad_parsers
from ..schemas import Player
from ..config.parser_indexes import CURRENT_YEAR


class SquadsSpider(scrapy.Spider):
    name = "squads"
    allowed_domains = ["transfermarkt.co.uk"]
    url = (
        "https://transfermarkt.co.uk/{squad}/kader/verein/{id}/saison_id/{year}/plus/1"
    )

    def __init__(self, season: str | None = None, clubs: dict | None = None) -> None:
        self.season = season
        self.clubs = clubs

    def parse(self, response: Response) -> Iterator[dict]:
        """
        Parse the response and yield a dictionary with the squad data.

        @url https://transfermarkt.co.uk/arsenal-fc/kader/verein/11/saison_id/2020/plus/1
        @returns items 1
        @scrapes dob age country current_club foot height joined_date name number position signed_from signing_fee tm_squad_id tm_squad value season squad
        """
        soup = self.soupify(response)

        if self.season != CURRENT_YEAR:
            index = f"pre-{CURRENT_YEAR}"
        else:
            index = CURRENT_YEAR

        parsers = get_squad_parsers(index=index)

        # concatenate parsers together
        data = pl.concat([parser(soup) for parser in parsers], how="horizontal")

        tm_squad_id = response.meta["tm_team_id"]
        tm_squad = response.meta["tm_team_name"]
        squad = response.meta["team_name"]
        league = response.meta["league"]

        if index == CURRENT_YEAR:  # current club is Null for 2024
            data = data.with_columns(current_club=pl.Series(values=[squad] * len(data)))

        data = data.with_columns(
            pl.Series("season", [self.season] * len(data)),
            pl.Series("tm_squad_id", [tm_squad_id] * len(data)),
            pl.Series("tm_squad", [tm_squad] * len(data)),
            pl.Series("squad", [squad] * len(data)),
            pl.Series("league", [league] * len(data)),
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
            for tm_team, id, squad in zip(
                row["tm_team_name"], row["tm_team_id"], row["team_name"]
            ):
                url = self.url.format(squad=tm_team, id=id, year=row["season"])

                yield scrapy.Request(
                    url=url,
                    callback=self.parse,
                    meta={
                        "tm_team_name": tm_team,
                        "tm_team_id": id,
                        "team_name": squad,
                        "league": row["league"],
                        "season": row["season"],
                    },
                )
