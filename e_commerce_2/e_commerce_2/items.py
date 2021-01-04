# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ECommerce2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Categories = scrapy.Field()
    Subcategories = scrapy.Field()
    Title = scrapy.Field()
    Description = scrapy.Field()
    Price = scrapy.Field()
    Review = scrapy.Field()

    pass
