import requests
import csv
from bs4 import BeautifulSoup

def get_hacker_new():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    first = soup.find('tr', class_ = 'athing')


    # getting text
    

    
    for f in first:
        title = f.find_next_sibling('tr').find('span', class_ = 'score')
        comments_ = f.find_next_sibling('tr').find_all('a')[-1].text
        author_ = f.find_next_sibling('tr').find('a', class_ = 'hnuser').text
        rank_ = f.find('span', class_ = 'rank').text.strip('.')

        if title:
            title = title.text
        else:
            title = "0 points"   

        if author_:
            author_ = author_.text
        else:
            author_ = "No author"

        data.append({
            'title': title,
            'link': link,
            'score': title,
            'comments':"{} comments" .format(comments_.split('')),
            'author': author_,
            'rank': rank_

        })

        return data

def csv_save(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

def main():
    hacker_news = get_hacker_new()
    csv_save(hacker_news, 'hacker_news.csv')


if __name__ == '__main__':
    main()