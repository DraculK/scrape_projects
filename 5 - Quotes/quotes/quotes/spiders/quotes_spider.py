import scrapy
from ..items import QuotesItem


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        items = QuotesItem()

        quotes = response.css("div.quote")
        for quote in quotes:
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("a.tag::text").extract()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items

        nextPage = response.css("li.next a::attr(href)").get()

        if nextPage:
            yield response.follow(nextPage, callback=self.parse)
