import scrapy
from ..items import ScrapingDevItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["web-scraping.dev"]
    start_urls = ["https://web-scraping.dev/products"]

    def parse(self, response):
        products = response.css('.row.product')
        for product in products:
            link = product.css("a::attr(href)").get()
            yield response.follow(link, callback=self.parseProducts)

        nextPage = response.css(".paging a::attr(href)").extract()
        if len(nextPage) == 6:
            yield response.follow(nextPage[5], callback=self.parse)

    def parseProducts(self, response):
        items = ScrapingDevItem()
        features = response.css(".product-features")

        items['name'] = response.css(".card-body h3::text").get()
        items['material'] = features.css(".feature-value::text").get()
        items['brand'] = features.css(".feature-value::text")[3].get()
        items['price'] = response.css(".product-price::text").get()
        items['image'] = response.css(".img-responsive::attr(src)").get()

        yield items
