import csv
import sys
import os
import json

from data.model.neoModel import Neo4jOperator
from data.wordCuter import wordCuter
from data.graphExecuter import GraphExecuter


class Executer:
    __path = ''

    __neoCon = None
    __wordCuter = None
    __graphExec = None

    def __init__(self):
        self.__path = os.getcwd()  # 获得程序入口目录
        self.__neoCon = Neo4jOperator(self.__path)  # 加载Neo4j数据库
        self.__wordCuter = wordCuter(self.__neoCon)  # 分词处理类
        self.__graphExec = GraphExecuter(self.__neoCon)  # 图处理类

    def __firstRun(self):
        filePath = self.__path + '/conf/global.json'
        if not(os.path.exists(filePath)):
            with open(filePath, 'w', encoding='UTF-8') as file:
                file.write('[{\n"isFirst" : true\n}]')
        with open(filePath, 'r', encoding='UTF-8') as f:
            conf = dict(json.load(f.read()))
            if(conf['isFirst']):
                self.__neoCon.init()

    def getCwdPath(self):
        '''
        封装 获取运行路径
        return 运行路径
        '''
        return self.__path

    def cutWords(self, key):
        '''分词
                key 表示要进行分词的字符串
                return 一串json字符串，用于前端显示
        '''
        return self.__wordCuter.cutWords(key)

    def getNodesAndRels(self, key):
        '''获得用于前端显示的gtfx序列
                key 根节点title
                return gtfx序列
        '''
        return self.__graphExec.nodeGen(key)
