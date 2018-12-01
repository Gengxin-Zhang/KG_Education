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

class EkdscrapyPipeline(object):
    def __init__(self):
        self.count = 0
        self.file = open('edu_wiki.json', 'w', encoding = 'UTF-8')
    def process_item(self, item, spider):
        if item['title']:
            line = ""
            if(self.count > 0):
                line += ","
            line += json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line)
            self.count += 1
            print("count: "+str(self.count)+'    '+item['title'])
            return item
        else:
            raise DropItem("忽略无title的组件！")
            
    def open_spider(self, spider):
        self.file.write("[\n")
        print("==================开启爬虫 \""+spider.name+"\" ==================")
        
    def close_spider(self, spider):
        self.file.write("\n]")
        print("==================关闭爬虫 \""+spider.name+"\" ==================")

