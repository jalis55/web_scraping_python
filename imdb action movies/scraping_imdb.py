import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/list/ls063897780/"


try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    data_set = soup.find_all("div", class_="lister-item mode-detail")
    titles = []
    ratings = []
    for data in data_set:
        title = data.find("h3")
        rating = data.find("span", class_="ipl-rating-star__rating")
        # links = data.find("a", href=True, class_="btn-full retina")["href"]
    print(titles)

except Exception as e:
    print(e)
