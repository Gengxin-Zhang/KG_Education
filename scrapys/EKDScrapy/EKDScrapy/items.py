# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #标题
    url = scrapy.Field()  #链接
    detail = scrapy.Field()  #内容
	

class EduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    words = scrapy.Field()  #词条组