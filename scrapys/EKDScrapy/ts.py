from langconv import Converter

file = open('edu_wiki.json', 'r', encoding = 'UTF-8')
wfile = open('edu_wiki_w.json', 'w', encoding = 'UTF-8')
cnt = 0

for line in file:
	strs = Converter('zh-hans').convert(line)
	wfile.write(strs)
	cnt += 1
	if(cnt % 100 == 0):
		print(str(cnt/15000) + '%')
