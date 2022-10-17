import requests
import csv
from bs4 import BeautifulSoup

def get_hacker_new():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    first = soup.find('tr', class_ = 'athing')


    # getting text
    title = first.find_next_sibling('tr').find('span', class_ = 'score')

    if title:
        title = title.text
    else:
        title = "0 points"

get_hacker_new()