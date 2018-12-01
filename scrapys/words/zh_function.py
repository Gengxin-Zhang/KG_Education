from langconv import *

file_object = open('edu_Math_words.txt','r',encoding='UTF-8').read()
str = Converter('zh-hans').convert(file_object)
strs = str.replace(',','\n')
open('edu_Math_words_zh.txt','w',encoding='UTF-8').write(strs)