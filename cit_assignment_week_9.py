import requests
import csv
from bs4 import BeautifulSoup

def get_hacker_new():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
