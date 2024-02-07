import scrapy
from ..items import ImdbItem


class Imdb250Spider(scrapy.Spider):
    name = "imdb250"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]
    headers = {
        'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                       "AppleWebKit/537.36 (KHTML,like Gecko) "
                       "Chrome/50.0.2661.102 Safari/537.36")
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.css("ul.ipc-metadata-list"
                              " li.ipc-metadata-list-summary-item")
        for movie in movies[:2]:
            href = movie.css("a::attr(href)").get()
            link = f"https://www.imdb.com/{href}"
            yield response.follow(link,
                                  callback=self.parseMovie,
                                  headers=self.headers)

    def parseMovie(self, response):
        items = ImdbItem()
        movieInfo = response.css(".sc-69e49b85-0")
        imdbInfo = response.css(".sc-3a4309f8-0")
        directionInfo = response.css(".sc-491663c0-10")
        name = movieInfo.css("span::text").get()
        year = movieInfo.css("a::text").get()
        duration = movieInfo.css("li.ipc-inline-list__item::text").get()
        rating = imdbInfo.css("span::text").get()
        popularity = imdbInfo.css("div.sc-5f7fb5b4-1::text").get()
        genres = directionInfo.css(".ipc-chip-list--baseAlt"
                                   " span::text").extract()
        director = directionInfo.css("a::text").get()

        items['name'] = name
        items['year'] = year
        items['duration'] = duration
        items['rating'] = rating
        items['popularity'] = popularity
        items['genres'] = genres
        items['director'] = director

        yield items
