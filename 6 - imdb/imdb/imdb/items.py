# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    rating = scrapy.Field()
    popularity = scrapy.Field()
    genres = scrapy.Field()
    director = scrapy.Field()
