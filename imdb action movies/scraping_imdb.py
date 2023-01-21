import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls063897780/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup()
