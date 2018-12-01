import csv
import json
import sys
import codecs

def trans():
    jsonData = open('edu_wiki_one_floor.json', 'r', encoding = 'utf-8')
    csvfile = open('data_with_detail.csv', 'w', newline='', encoding = 'utf-8') # python3下
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    dic = json.load(jsonData)
    flag = True
    for line in dic:
        if flag:
            # 获取属性列表
            keys = list(line.keys())
            print (keys)
            writer.writerow(keys) # 将属性列表写入csv中
            flag = False
        # 读取json数据的每一行，将values数据一次一行的写入csv中
        strs = list(line.values())
        strs[-1] = strs[-1].replace('\n','\\n')
        writer.writerow(strs)
    jsonData.close()
    csvfile.close()
	
if __name__ == '__main__':
    trans()