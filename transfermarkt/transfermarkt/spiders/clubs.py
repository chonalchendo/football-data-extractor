from urllib.parse import parse_qs, urlparse

import scrapy
from bs4 import BeautifulSoup

from ..config.leagues import league_map


class ClubsSpider(scrapy.Spider):
    name = "clubs"
    allowed_domains = ["transfermarkt.co.uk"]
    base_url = "https://transfermarkt.co.uk/{league}/startseite/wettbewerb/{league_id}/plus/?saison_id={year}"

    def __init__(self, leagues=None, seasons=None, *args, **kwargs):
        super(ClubsSpider, self).__init__(*args, **kwargs)
        # self.leagues = leagues.split(", ") if leagues else []
        # self.seasons = seasons.split(", ") if seasons else []
        match leagues:
            case "all":
                self.leagues = list(league_map.keys())
            case leagues if leagues is None:
                raise ValueError("No leagues provided")
            case _:
                self.leagues = leagues.split(", ")

        match seasons:
            case "all":
                self.seasons = [str(i) for i in range(2018, 2024)]
            case seasons if seasons is None:
                raise ValueError("No seasons provided")
            case _:
                self.seasons = seasons.split(", ")

    def parse(self, response):
        """
        Parse the response and extract the team names and ids

        @url https://transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2018
        @returns items 1
        @scrapes league season team_name team_id
        """
        soup = BeautifulSoup(response.text, "html.parser")
        team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
        team_name = [td.find("a").get("href").split("/")[1] for td in team_info]
        team_id = [td.find("a").get("href").split("/")[4] for td in team_info]

        # get league and season from the url
        url = response.url
        league = urlparse(url).path.split("/")[1]
        season = parse_qs(urlparse(url).query)["saison_id"][0]

        yield {
            "league": league,
            "season": season,
            "team_name": team_name,
            "team_id": team_id,
        }

    def start_requests(self):
        """
        Start the requests for the given leagues and seasons.
        @returns request 1
        """
        # match self.leagues:
        #     case 'all':
        #         self.leagues = list(league_map.keys())
        #     case self.leagues if len(self.leagues) == 0:
        #         raise ValueError("No leagues provided")
        #     case _:
        #         pass
        #
        # match self.seasons:
        #     case 'all':
        #         self.seasons = [str(i) for i in range(2018, 2024)]
        #     case self.seasons if len(self.seasons) == 0:
        #         raise ValueError("No seasons provided")
        #     case _:
        #         pass

        for season in self.seasons:
            for league in self.leagues:

                url = self.base_url.format(
                    league=league, league_id=league_map.get(league), year=season
                )
                yield scrapy.Request(url, callback=self.parse)
