# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv
import sys
import time
from scrapy.exceptions import DropItem
from scrapy import log

class WikiwordsscrapyPipeline(object):
    def __init__(self):
        self.count = 0
        self.file = open('result.txt', 'w')
    def process_item(self, item, spider):
        if item['name']:
            self.file.write(item['name'])
            self.count += 1
            print("count: "+str(self.count)+'    '+item['name'])
            return item
        else:
            raise DropItem("忽略无title的组件！")
            
    def open_spider(self, spider):
        print("==================开启爬虫 \""+spider.name+"\" ==================")
        
    def close_spider(self, spider):
        self.file.write("\n")
        print("==================关闭爬虫 \""+spider.name+"\" ==================")
