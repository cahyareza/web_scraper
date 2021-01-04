#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:21:44 2020

@author: apple
"""

import scrapy
from practicalone.items import PracticaloneItem

class SolutionSpider(scrapy.Spider):
    name = "Solution"
    start_urls = [
        "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
        "https://books.toscrape.com/catalogue/soumission_998/index.html",
        "https://books.toscrape.com/catalogue/sharp-objects_997/index.html",
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",        
        ]
    
    def parse(self, response):
        item = PracticaloneItem()
        
        item['title'] = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        
        item['price'] = response.xpath('//p[@class="price_color"]/text()').get()
        
        item['category'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        
        item['in_stock'] = response.xpath('normalize-space(//p[@class="instock availability"]/i/following::node()[1])').get()
      
        return item