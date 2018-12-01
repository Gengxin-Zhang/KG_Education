import json
from lxml import etree

with open('edu_wiki.json', 'r', encoding = 'UTF-8') as file:
	with open('edu_wiki_one_floor.json', 'w', encoding = 'UTF-8') as save:
		data = json.load(file)
		save.write('[\n')
		count = 0
		flag = False
		for line in data:
			count += 1
			ks = list(line.keys())
			vs = list(line.values())
			page = vs[-1]
			selectors = etree.HTML(page).xpath('//div[@class="mw-parser-output"]/*')
			if(count == 420):
				print(selectors[-1])
			for selector in selectors:
				if(selector.xpath('attribute::class') == 'metadata plainlinks ambox ambox-content'):
					continue
				if(selector.xpath('./span') != []):
					break
				vs[-1] = ''
				vs[-1] = vs[-1] + etree.tostring(selector, method='html').decode('utf-8')
			if(flag):
				save.write(',')
			flag = True
			strs = '{ '
			cnt = 0
			item = {'title':'', 'url':'', 'detail':''}
			for key in ks:
				item[key] = vs[cnt]
				cnt += 1
			save.write(json.dumps(item,ensure_ascii=False) + "\n")
		save.write(']')