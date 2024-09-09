import scrapy
from bs4 import BeautifulSoup

from ..config.leagues import league_map


class ClubsSpider(scrapy.Spider):
    name = "clubs"
    allowed_domains = ["transfermarkt.co.uk"]
    base_url = "https://transfermarkt.co.uk/{league}/startseite/wettbewerb/{league_id}/plus/?saison_id={year}"

    def __init__(self, leagues=None, seasons=None, *args, **kwargs):
        super(ClubsSpider, self).__init__(*args, **kwargs)
        self.leagues = leagues.split(", ") if leagues and leagues != 'all' else []
        self.seasons = seasons.split(", ") if seasons and seasons != 'all' else []

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser') 
        team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
        team_name = [td.find("a").get("href").split("/")[1] for td in team_info]
        team_id = [td.find("a").get("href").split("/")[4] for td in team_info]
        yield {"team_name": team_name, "team_id": team_id}



    def start_requests(self):

        match self.leagues:
            case 'all':
                self.leagues = list(league_map.keys())
            case self.leagues if len(self.leagues) == 0:
                raise ValueError("No leagues provided")
            case _:
                pass

        match self.seasons:
            case 'all':
                self.seasons = [str(i) for i in range(2018, 2024)]
            case self.seasons if len(self.seasons) == 0:
                raise ValueError("No seasons provided")
            case _:
                pass

        for season in self.seasons:
            for league in self.leagues:
                url = self.base_url.format(
                    league=league, 
                    league_id=league_map.get(league), 
                    year=season
                )
                yield scrapy.Request(url, callback=self.parse)


