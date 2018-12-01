import jieba.posseg as pseg
import json
from data.model.neoModel import Neo4jOperator
from app.models.wiki import Wiki

def preok(s):
    '''对某一个词进行词性筛选，此函数筛选能进行拼词的前一个词应当满足什么词性条件
            s 表示进行词性筛选的词性
            return 返回这个词性是否满足条件
    '''
    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz' or s == 'l':
        return True
    if s == 'v' or s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 'u':
        return True
    if s == 't' or s == 'm':
        return True
    return False


def nowok(s):
    '''对某一个词进行词性筛选，此函数筛选单个词或者能进行拼词的后一个词应当满足什么词性条件
            s 表示进行词性筛选的词性
            return 返回这个词性是否满足条件
    '''
    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz' or s == 'l' or s == 'eng':
        return True
    if s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 't':
        return True
    if s == 't' or s == 'm':
        return True
    return False


class wordCuter:
    '''分词处理类'''

    def __init__(self, con):
        self.__neoCon = con

    def cutWords(self, key):
        ''' 使用thulac进行分词 TagList[i][0]代表第i个词
                TagList[i][1]代表第i个词的词性
                key 表示欲进行分词的字符串
                return json格式的字符串，前端显示以此json为模型
        '''
        key = key.strip()
        result = []
        for tag, flag in pseg.cut(key):
            item = {}
            item["word"] = tag
            item["is_node"] = False
            word = self.__neoCon.matchItembyTitle(tag)
            if word:
                item["url"] = '/wiki/' + tag
                item["is_node"] = True
                item["content"] = Wiki.objects.filter(name=tag)[0].content[:50]+'...'
            result.append(item)
        return result
