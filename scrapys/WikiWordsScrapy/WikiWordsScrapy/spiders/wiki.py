import scrapy
from WikiWordsScrapy.items import WikiItem
from WikiWordsScrapy.spiders.langconv import *
import urllib
import os

split_sign = '##'  # 定义分隔符

class WikiSpider(scrapy.Spider):
	name = "wiki"   #爬虫启动命令：scrapy crawl wiki
	allowed_domains = ["zh.wikipedia.org"]    #声明地址域
	
#	file_object = open('merge_table3.txt','r').read()
	file_object = open('edu_Math_words_zh.txt','r',encoding='UTF-8').read()
	wordList = file_object.split('\n')  # 获取词表
	
	start_urls = []
	count = 0
	
  # 本处是用于构造原始json
	for i in wordList:    ##生成url列表
		cur = "https://zh.wikipedia.org/wiki/"
		cur = cur + str(i)
		start_urls.append(cur)
#		count += 1
		#print(cur)
#		if count > 1000:
#			break	

	def parse(self, response):		
		# div限定范围
		main_div = response.xpath('//div[@id="mw-content-text"]/div[@class="mw-parser-output"]')
		links = main_div.xpath('./p[1]/a')
		item = WikiItem()
		name = ""
		for link in links:
			str = link.xpath('string(.)').extract()
			str = Converter('zh-hans').convert(str)
			name += str + '\n'
		item['name'] = name
		yield item 