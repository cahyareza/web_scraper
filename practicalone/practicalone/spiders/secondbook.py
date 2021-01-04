#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:42:13 2020

@author: apple
"""

import scrapy
from practicalone.items import PracticaloneItem

class SecondSpider(scrapy.Spider):
    name = "Books2"
    start_urls =[
    
        'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
    
    ]
    
    def parse(self,response):
        #add objects
        item = PracticaloneItem()
        #accessing items attribute
        #item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        #item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        # to reserve specific
        item['price'] = response.xpath('//p[@class="price_color"]/text()').get()
        
        return item
    