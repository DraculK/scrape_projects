# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingDevItem(scrapy.Item):
    name = scrapy.Field()
    material = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
