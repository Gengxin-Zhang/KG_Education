import json
from py2neo import Node, Relationship ,Graph
from langconv import *
import re
class loadDatatoNeo4j(object):
	graph = None
	def __init__(self):
		print("start load data ...")
	def connectDB(self):
		self.graph = Graph("http://localhost:7474",username = "neo4j" , password = "123456")
		print("connect neo4j success!")

	def readData(self):
		count = 0
		passcnt = 0
		with open("new_node.csv",'w',encoding='UTF-8') as fw:
			fw.write("title,lable"+'\n')
		with open("wikidata_relation.csv","w",encoding='UTF-8') as fw:
			fw.write("Item1,relation,Item2"+'\n')
		with open("wikidata_relation2.csv","w",encoding='UTF-8') as fw:
			fw.write("Item,relation,NewNode"+'\n')
		with open("../wikidataRelation/entityRelation.json","r", encoding = 'UTF-8') as fr:
			with open("new_node.csv",'a',encoding='UTF-8') as fwNewNode:
				with open("wikidata_relation.csv",'a',encoding='UTF-8') as fwWikidataRelation:
					with open("wikidata_relation2.csv",'a',encoding='UTF-8') as fwWikidataRelation2:
						newNodeList = list()
						for line in fr:
							# print(line)
							entityRelationJson = json.loads(line)
							entity1 = entityRelationJson['entity1']
							entity1 = entity1.replace('\n','')
							entity2 = entityRelationJson['entity2']
							#搜索entity1
							find_entity1_result = self.graph.find_one(
								property_key = "title" ,
								property_value = entity1,
								label = "Item"
							)
							#搜索entity2
							find_entity2_result = self.graph.find_one(
								property_key = "title",
								property_value = entity2,
								label = "Item"
							)
							count += 1
							if(count % 1000 == 0):
								print(str(count/1700)+'%')
							# 如果entity1不在实体列表中(emmmmmm,不可能吧)，那么就不要继续了
							if(find_entity1_result is None):
								passcnt += 1
								if(passcnt % 1000 == 0):
									print('pass ' + str(passcnt))
								continue

							#去掉entityRelationJson['relation']中的逗号和双引号
							entityRelationList = re.split(",|\"",entityRelationJson['relation'])
							entityRelation = ""
							for item in entityRelationList:
								entityRelation = entityRelation + item
							#去掉entity2字符串中的逗号,并将繁体转成简体
							entity2List = re.split(",|\"",entity2)
							entity2 = "" 
							for item in entity2List:
								entity2 = entity2 + item
							entity2 = Converter('zh-hans').convert(entity2)

							# 如果entity2既不在实体列表中，又不在NewNode中，则新建一个节点，该节点的lable为newNode，然后添加关系
							if(find_entity2_result is None):
								if(entity2 not in newNodeList):
									fwNewNode.write(entity2+","+"newNode"+'\n')
									newNodeList.append(entity2)
								fwWikidataRelation2.write(entity1+","+entityRelation+","+entity2+'\n')
							#如果entity2在实体列表中，直接连关系即可
							else:
								fwWikidataRelation.write(entity1+","+entityRelation+","+entity2+'\n')

if __name__ == "__main__":
	loadData = loadDatatoNeo4j()
	loadData.connectDB()
	loadData.readData()
