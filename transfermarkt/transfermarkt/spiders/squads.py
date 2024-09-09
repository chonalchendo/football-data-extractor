import scrapy


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

    def parse(self, response):
        pass

    def start_requests(self):
        self.url.format(name, id, year)
