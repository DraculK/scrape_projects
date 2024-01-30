import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                   "AppleWebKit/537.36 (KHTML,like Gecko) Chrome/50.0.2661.102"
                   " Safari/537.36")
    }

r = requests.get(url, headers=headers)
html_content = r.text

soup = BeautifulSoup(html_content, "html.parser")

# main ul with all data
ul = soup.find("ul", {"class": "ipc-metadata-list"})
# li with all movie divs
li = ul.findAll("li", {"class": "ipc-metadata-list-summary-item"})

names = []
years = []
rates = []

for tag in li:
    # name
    name = tag.find("h3", {"class": "ipc-title__text"})
    names.append(name.text.split(".")[1][1:])
    # year
    year = tag.find(
        "span",
        {"class": "sc-1e00898e-8 hsHAHC cli-title-metadata-item"}
    )
    years.append(year.text)
    # rating
    rate = tag.find("span", {"class": "ipc-rating-star"})
    rates.append(rate.text[:3])

with open('imdb.csv', "w", encoding='UTF-8') as f:
    field_names = ['name', 'year', 'rate']
    imdb_writer = csv.DictWriter(f, delimiter=';',
                                 fieldnames=field_names,
                                 lineterminator='\n')
    imdb_writer.writeheader()
    for i in range(len(names)):
        imdb_writer.writerow({
            "name": names[i],
            "year": years[i],
            "rate": rates[i]
        })
