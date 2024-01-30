import json
import requests
from bs4 import BeautifulSoup

quotes = []
authors = []

for page in range(11):
    url = f"https://quotes.toscrape.com/page/{page}"
    r = requests.get(url)
    html_content = r.text

    soup = BeautifulSoup(html_content, 'html.parser')

    for tag in soup.findAll('span', {'class': 'text'}):
        quotes.append(tag.text[1:-1])

    for tag in soup.findAll('small', {'class': 'author'}):
        authors.append(tag.text)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(
        [{'author': author, 'quote': quote} for author, quote
         in zip(authors, quotes)],
        f
    )
