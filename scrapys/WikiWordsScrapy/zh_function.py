from langconv import *

file_object = open('result.txt','r',encoding='UTF-8').read()
str = Converter('zh-hans').convert(file_object)
strList = str.split('\n')
strList = list(set(strList))
strList.sort()
f = open('edu_Math_words_zh_sorted.txt','w',encoding='UTF-8')
for s in strList:
	f.write(s+'\n')