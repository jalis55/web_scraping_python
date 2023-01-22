import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.imdb.com/list/ls063897780/"
url = "https://www.imdb.com/list/ls063897780/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"


try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    data_set = soup.find_all("div", class_="lister-item mode-detail")
    titles = []
    ratings = []
    links = []

    for data in data_set:
        title = data.find("h3", class_="lister-item-header")
        title = title.find("a").text
        rating = data.find("span", class_="ipl-rating-star__rating").text
        link = data.find("a", href=True)['href']
        titles.append(title)
        ratings.append(rating)
        links.append("www.imdb.com"+link)
    data = {
        "Title": titles,
        "Ratings": ratings,
        "Links": links
    }
    df = pd.DataFrame(data)
    df.to_csv("imdb.csv", index=False)
except Exception as e:
    print(e)
