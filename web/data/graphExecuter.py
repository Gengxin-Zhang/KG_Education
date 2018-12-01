import json
import jieba
from data.model.neoModel import Neo4jOperator

head = """
<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2" xmlns:viz="http://www.gexf.net/1.2draft/viz" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd">
  <meta lastmodifieddate="2014-01-30">
    <creator>Gephi 0.8.1</creator>
    <description></description>
  </meta>
  <graph defaultedgetype="undirected" mode="static">
    <attributes class="node" mode="static">
      <attribute id="modularity_class" title="Modularity Class" type="integer"></attribute>
    </attributes>
        """
tail = """
  </graph>
</gexf>

        """

class GraphExecuter:
    '''图处理类'''
    __neoCon = None

    __pt = 0
    __pt2 = 0
    __ns = []
    __rs = []

    def __init__(self, con):
        self.__neoCon = con
        if(self.__neoCon == None):
            print("GraphExecuter loaded with error!")
        else:
            print("GraphExecuter loaded successfully!")

    def __nodeGEXF(self, node, id, classfor):
        '''生成单个Node的GEXF标签
                node 标签对象
                id 编号
                return node标签字符串
        '''
        title = node['title']
        strs = '<node id="%d" label="%s"><attvalues><attvalue value="%d" for="modularity_class"/></attvalues></node>'%(id, title, classfor)
        return strs

    def __relationGEXF(self, edge, id, source, target):
        '''生成单个Edge的GEXF标签
                edge 标签对象
                id 编号
                source 起始Node节点的编号
                target 结束Node节点的编号
                return node标签字符串
        '''
        property = edge['property']
        strs = '<edge id="' + str(id) + '" source="' + str(source) + '" ' + ' target="' + str(target) + '"></edge>'
        return strs

    def __addNode(self, node, classfor):
        '''添加Node节点的重构函数
                node 添加的node对象
                classfor node对象所属分类
                return node标签字符串
        '''
        if(node != None):
            if not(node in self.__ns):
                self.__ns.append(node)
                self.__pt += 1
                return self.__nodeGEXF(node, self.__pt, classfor)
        return ''

    def __nodeInNs(self, node):
        '''寻找指定的node对象的编号
                node 欲寻找编号的node对象
                return 编号，不在组内返回-1
        '''
        index = 0
        for n in self.__ns:
            index += 1
            if(n == node):
                return index
        return -1

    def __addRelation(self, node1, node2, rel):
        '''添加Relation节点的重构函数
                node1 关系的开始点
                node2 关系的结束点
                rel 添加的relation对象
                return edge标签字符串
        '''
        if(rel != None):
            if not(rel in self.__rs):
                self.__rs.append(rel)
                self.__pt2 += 1
                return self.__relationGEXF(rel, self.__pt2, self.__nodeInNs(node1), self.__nodeInNs(node2))
        return ''

    def __clear(self):
        self.__pt = 0
        self.__pt2 = 0
        self.__ns = []
        self.__rs = []

    def nodeGen(self, value):
        ''' 生成用于前端显示的gtfx序列
                key 表示根节点title
                return gtfx序列，用于前端显示图
        '''
        words = jieba.cut_for_search(value)
        categories = []
        nodes = '<nodes>'
        relations = '<edges>'
        for word in words:
            iResult = self.__neoCon.getEntityRelationsbyEntity(word)
            if iResult:
                categories.append(word)
                for line in iResult:
                    nodes = nodes + self.__addNode(line['a'], len(categories)-1)
                    nodes = nodes + self.__addNode(line['c'], len(categories)-1)
                    relations = relations + \
                        self.__addRelation(line['a'], line['c'], line['b'])
                    nodes = nodes + self.__addNode(line['e'], len(categories)-1)
                    relations = relations + \
                        self.__addRelation(line['c'], line['e'], line['d'])
                    nodes = nodes + self.__addNode(line['g'], len(categories)-1)
                    relations = relations + \
                        self.__addRelation(line['e'], line['g'], line['f'])

        nodes = nodes + '</nodes>'
        relations = relations + '</edges>'
        self.__clear()
        return {
            'categories': categories, 
            'graphData': head + nodes + relations + tail
            }
