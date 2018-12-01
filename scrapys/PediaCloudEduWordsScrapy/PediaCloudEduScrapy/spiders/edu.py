
import scrapy
from PediaCloudEduScrapy.items import PediacloudeduscrapyItem
import urllib

class WikiSpider(scrapy.Spider):
	name = "edu"   #爬虫启动命令：scrapy crawl edu
	allowed_domains = ["pedia.cloud.edu.tw"]    #声明地址域
	
	start_urls = []
#	count = 0
	
	for i in range(1,194):    ##生成url列表
		cur = "http://pedia.cloud.edu.tw/NavigateWord/list/"
		cur = cur + str(i) + "?id=6"
		start_urls.append(cur)
#		count += 1
		#print(cur)
#		if count > 1000:
#			break	

	def parse(self, response):		
		#限定范围
		main_div = response.xpath('//table[@class="table table-striped table-condensed"]')
		words = ""
		for i in main_div.xpath('./tbody/tr/td[1]/a'):
			words = words + i.xpath('string(.)').extract()[0].strip() + ","
		item = PediacloudeduscrapyItem()
		item['words'] = words
		yield item