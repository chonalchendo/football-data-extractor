from bs4 import BeautifulSoup


def get_squad_name(soup: BeautifulSoup) -> str:
    return soup.find(class_="data-header").find("h1").text.strip()
