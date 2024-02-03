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
durations = []
main_genre = []

for tag in li:
    # year
    year = tag.find(
        "span",
        {"class": "sc-be6f1408-8 fcCUPU cli-title-metadata-item"}
    )
    years.append(year.text)

    # rating
    rate = tag.find("span", {"class": "ipc-rating-star"})
    rates.append(rate.text[:3])

    # duration
    duration = tag.find(
        "div",
        {"class": "sc-be6f1408-7 iUtHEN cli-title-metadata"}
    )
    durations.append(f"{duration.text[4:].split('m')[0]}m")

    link = tag.find("a", {"class": "ipc-title-link-wrapper"})
    movie_url = f"https://www.imdb.com{link['href']}"

    movie_r = requests.get(movie_url, headers=headers)
    movie_html = movie_r.text
    movie_soup = BeautifulSoup(movie_html, "html.parser")

    # name
    name = movie_soup.find("span", {"class": "hero__primary-text"})
    names.append(name.text)

    # genre
    main_genre = movie_soup.find("span", {"class": "ipc-chip__text"})
    main_genre.append(main_genre.text)

with open('imdb.csv', "w", encoding='UTF-8') as f:
    field_names = ['name', 'year', 'rate', 'duration', 'main_genre']
    imdb_writer = csv.DictWriter(f, delimiter=';',
                                 fieldnames=field_names,
                                 lineterminator='\n')
    imdb_writer.writeheader()
    for i in range(len(names)):
        imdb_writer.writerow({
            "name": names[i],
            "year": years[i],
            "rate": rates[i],
            "duration": durations[i],
            "main_genre": main_genre[i]
        })
