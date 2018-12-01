import scrapy
from EKDScrapy.items import WikiItem
from EKDScrapy.spiders.langconv import *
from lxml import etree
import urllib

class WikiSpider(scrapy.Spider):
	name = "wiki"   #爬虫启动命令：scrapy crawl wiki
	allowed_domains = ["zh.wikipedia.org"]
	
	file_object = open('edu_Math_words_zh.txt','r',encoding='UTF-8').read()
	wordList = file_object.split('\n')
	
	start_urls = []
	count = 0
	
	for i in wordList:
		cur = "https://zh.wikipedia.org/wiki/"
		cur = cur + str(i)
		start_urls.append(cur)
		count += 1
#		#print(cur)
		if count > 10:
			break	

	def parse(self, response):
		main_div = response.xpath('//div[@id="mw-content-text"]/div[@class="mw-parser-output"]')
		title = response.url.split('https://zh.wikipedia.org/wiki/')[-1]
		title = urllib.parse.unquote(title)
		error = response.xpath('//div[@id="mw-content-text"]/div[@class="noarticletext mw-content-ltr"]/div[@id="noarticletext"]/p/b')
		errorMsg = error.extract()
		if errorMsg != []:
			title = 'error'
		title = Converter('zh-hans').convert(title)
		url = response.url
		url = urllib.parse.unquote(url)
		detail = etree.tostring(main_div, method='html').decode('utf-8')
		item = WikiItem()
		item['title'] = title
		item['url'] = url
		item['detail'] = detail
		yield item 