from py2neo import Graph, Node, Relationship, cypher, Path
import neo4j
import os
import json


class Neo4jOperator():
    '''用于操作neo4j数据库的操作类'''
    __graph = None  # py2neo通过此对象对整个数据库进行操作
    __path = ''

    def __connectDB(self):
        '''通过读取json格式的配置文件连接到数据库'''
        filePath = self.__path + "/data/conf/neo4j.json"
        if not(os.path.exists(filePath)):
            print("neo4j configuration doesn't exist!")
            return
        with open(filePath, "r", encoding="UTF-8") as conf:
            item = list(json.load(conf)[0].values())
            print(item)
            self.__graph = Graph(
                address=item[0], username=item[1], password=item[2])

    def __init__(self, path):
        self.__path = path
        self.__connectDB()
        if(self.__graph != None):
            print("Successfully connect to neo4j database!")
        else:
            print("Unable to connect to neo4j database!")

    def matchItembyTitle(self, value):
        '''检索数据库中的Item实体信息
                value 用于检索的Item实体的title
                return 返回一个py2neo中node类的list，node类可以用dict方式直接访问
        '''
        cql = "MATCH (n:Item { title: '%s' }) return n;" % value
        answer = self.__graph.run(cql).data()
        return answer

    def getEntityRelationsbyEntity(self, value):
        '''获取4层的节点关系
                value 起始节点的title
                return 含有所有查询到的节点和关系的list
        '''
        cql = 'MATCH (a:Item{title:"%s"})-[b:rel]->(c)-[d]->(e)-[f]->(g)  RETURN a,b,c,d,e,f,g LIMIT 10' % value
        answer = self.__graph.run(cql).data()
        cql = 'MATCH (a)-[b:rel]->(c)-[d]->(e)-[f]->(g:Item{title:"%s"})  RETURN a,b,c,d,e,f,g LIMIT 10' % value
        answer+=self.__graph.run(cql).data()
        return answer

    def getEntityRelationbyEntity(self, value):
        '''根据entity的名称返回关系'''
        answer = self.__graph.run(
            'MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.title = "%s" RETURN rel,entity2' % value).data()
        return answer

    def findRelationByEntity(self, entity1):
        '''查找entity1及其对应的关系（与getEntityRelationbyEntity的差别就是返回值不一样）'''
        answer = self.__graph.run(
            'MATCH (n1 {title:"%s"})- [rel] -> (n2) RETURN n1,rel,n2' % entity1).data()
        return answer

    def findRelationByEntity2(self, entity1):
        '''查找entity2及其对应的关系'''
        answer = self.__graph.run(
            'MATCH (n1)- [rel] -> (n2 {title:"%s"}) RETURN n1,rel,n2' % entity1).data()
        return answer

    def findOtherEntities(self, entity, relation):
        '''根据entity1和关系查找entity2'''
        answer = self.__graph.run(
            'MATCH (n1 {title:"%s"})- [rel {type:"%s"}] -> (n2) RETURN n1,rel,n2' % (entity, relation)).data()
        return answer

    def findOtherEntities2(self, entity, relation):
        '''根据entity2和关系查找entity1'''
        answer = self.__graph.run(
            'MATCH (n1)- [rel {type:"+%s+"}] -> (n2 {title: "%s" }) RETURN n1,rel,n2'%(relation,entity)).data()
        return answer

    def findRelationByEntities(self, entity1, entity2):
        '''根据两个实体查询它们之间的最短路径'''
        answer = self.__graph.run(
            'MATCH (p1:Item {title:"%s"}),(p2:Item{title:"%s"}),\
                    p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN rel'%(entity1,entity2)).evaluate()
        if not answer:
            answer = self.__graph.run(
                'MATCH  (p1:Item {title:"%s"}),\
                        (p2:NewItem {title:"%s"}),\
                        p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p'%(entity1, entity2)).evaluate()
        if not answer:
            answer = self.__graph.run(
                'MATCH  (p1:NewItem {title:"%s"}),\
                        (p2:Item{title:"%s"}),\
                        p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p'%(entity1,entity2)).evaluate()
        if not answer:
            answer = self.__graph.run(
                'MATCH  (p1:NewItem {title:"%s"}),\
                        (p2:NewItem {title:"%s"}),\
                        p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p'%(entity1,entity2)).evaluate()

        relationDict = []
        if answer:
            for x in answer:
                tmp = {}
                start_node = x.start_node
                end_node = x.end_node
                tmp['n1'] = start_node
                tmp['n2'] = end_node
                tmp['rel'] = x
                relationDict.append(tmp)
        return relationDict

    def findEntityRelation(self, entity1, relation, entity2):
        '''查询数据库中是否有对应的实体-关系匹配'''
        answer = self.__graph.run(
            'MATCH (n1:Item {title:"%s"})- [rel:RELATION {type:"%s"}] -> (n2:Item{title:"%s"}) RETURN n1,rel,n2'%(entity1, relation, entity2)).data()
        if not answer:
            answer = self.__graph.run(
                'MATCH (n1:Item {title:"%s"})- [rel:RELATION {type:"%s"}] -> (n2:NewItem{title:"%s"}) RETURN n1,rel,n2'%(entity1, relation, entity2)).data()
        if not answer:
            answer = self.__graph.run(
                'MATCH (n1:NewItem {title:"%s"})- [rel:RELATION {type:"%s"}] -> (n2:Item{title:"%s"}) RETURN n1,rel,n2'%(entity1, relation, entity2)).data()
        if not answer:
            answer = self.__graph.run(
                'MATCH (n1:NewItem {title:"%s"})- [rel:RELATION {type:"%s"}] -> (n2:NewItem{title:"%s"}) RETURN n1,rel,n2'%(entity1, relation, entity2)).data()

        return answer
