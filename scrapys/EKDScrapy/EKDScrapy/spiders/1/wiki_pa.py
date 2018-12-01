import scrapy
from EKDScrapy.items import WikiItem
from EKDScrapy.spiders.langconv import *
import urllib

split_sign = '##'  # 定义分隔符

class WikiSpider(scrapy.Spider):
	name = "wiki_pa"   #爬虫启动命令：scrapy crawl wiki_pa
	allowed_domains = ["zh.wikipedia.org"]    #声明地址域
	
#	file_object = open('merge_table3.txt','r').read()
	file_object = open('crawled_leaf_list.txt','r',encoding='UTF-8').read()
	wordList = file_object.split('\n')  # 获取词表
	
	start_urls = []
	count = 0
	
  # 本处是用于构造原始json
	for i in wordList:    ##生成url列表
		cur = "https://zh.wikipedia.org/wiki/"
		temp = str(i).split(':')
		tempcnt = 0
		tempstr = ''
		flag = 0
		for j in temp:
			tempcnt = tempcnt + 1
			if tempcnt <= 2 :
				continue
			if flag :
				tempstr += ':'
			tempstr += j
			flag = 1
		cur = cur + tempstr
		start_urls.append(cur)
		count += 1
		#print(cur)
		if count > 2:
			break	

	def parse(self, response):		
		# div限定范围
		main_div = response.xpath('//div[@id="mw-content-text"]/div[@class="mw-parser-output"]')
		
		title = response.url.split('https://zh.wikipedia.org/wiki/')[-1]  #  通过截取url获取title
		title = urllib.parse.unquote(title)
		if title.find('isFrom=intoDoc') != -1:
			title = 'error'
		title = Converter('zh-hans').convert(title)
		url = response.url   # url直接得到
		url = urllib.parse.unquote(url)
		
		img = ""   # 爬取图片url
		for p in main_div.xpath('.//div[@class="thumb tright"]//img[@class="thumbimage"]/@src'):
			img = p.extract().strip()
			
		detail = "" # 详细信息
		detail_xpath = main_div.xpath('./p')
		if len(detail_xpath) > 0 :   
			detail = Converter('zh-hans').convert(detail_xpath.xpath('string(.)').extract()[0].strip())
		
		item = WikiItem()
		item['title'] = title
		item['url'] = url
		item['image'] = img
		item['detail'] = detail
		yield item 