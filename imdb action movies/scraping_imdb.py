import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls063897780/"


try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    data = soup.find_all("div", class_="lister-item mode-detail")
    print(data[0])
except Exception as e:
    print(e)
