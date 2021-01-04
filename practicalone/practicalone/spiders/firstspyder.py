# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#section 1
import scrapy
from scrapy.crawler import CrawlerProcess


#section 2
class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        
        "https://books.toscrape.com",
    ]

    def parse(self, response):
        return response.body