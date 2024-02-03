import requests
from bs4 import BeautifulSoup

movieName = input("Coloque o nome de um filme: ").lower()

url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                   "AppleWebKit/537.36 (KHTML,like Gecko) Chrome/50.0.2661.102"
                   " Safari/537.36")
    }

res = requests.get(url, headers=headers)
html_content = res.text
soup = BeautifulSoup(html_content, 'html.parser')

# main ul with all data
ul = soup.find("ul", {"class": "ipc-metadata-list"})
# li with all movie divs
li = ul.findAll("li", {"class": "ipc-metadata-list-summary-item"})

for tag in li:
    link = tag.find("a", {"class": "ipc-title-link-wrapper"})
    movie_url = f"https://www.imdb.com{link['href']}"

    movie_r = requests.get(movie_url, headers=headers)
    movie_html = movie_r.text
    movie_soup = BeautifulSoup(movie_html, "html.parser")

    # name
    name = movie_soup.find(
        "span", {"class": "hero__primary-text"}
        ).text

    if movieName == name.lower():
        print(f"Se gostou de {name}, também pode gostar de: ")
        titles = movie_soup.findAll("span", {"data-testid": "title"})
        for title in titles:
            print(title.text)
        break
    else:
        print("O filme não está no nosso banco de dados.")
