import json
from py2neo import Node, Relationship ,Graph, NodeMatcher
from langconv import *
import re

graph = Graph("http://localhost:7474",username = "neo4j" , password = "123456")

with open("node.txt",'w',encoding='UTF-8') as fw:
	matcher = NodeMatcher(graph)
	math = matcher.match("Item", title = "数学").first()
	ts = math.nodes()
	for t1 in ts:
		print(t1)
		ts1 = t1.nodes()
		for t2 in ts1:
			print(t2)
			ts2 = t2.nodes()
			for t3 in ts2:
				print(t3)
			for r2 in t2.relationships():
				print(r2)
		for r1 in t1.relationships():
			print(r1)
