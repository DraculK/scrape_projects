import json
import requests

quotes = []
authors = []

for page in range(11):
    url = f"https://quotes.toscrape.com/page/{page}"
    r = requests.get(url)

    html_content = r.text.split("\n")

    for line in html_content:
        if '<span class="text" itemprop="text">' in line:
            quotes.append(line[44:].split("”")[0])
        if '<small class="author" itemprop="author">' in line:
            authors.append(line[57:].split("<")[0])

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(
        [{'author': author, 'quote': quote} for author, quote
         in zip(authors, quotes)],
        f
    )
