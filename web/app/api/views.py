from data import executer
from flask import Response, flash, Blueprint, request, g
from flask import redirect, render_template, render_template_string, jsonify, request
import json
from app.common import trueReturn, falseReturn
from app.models.wiki import User, Wiki

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/search', methods=['POST', 'GET'])
def search():
    """ search : 查一下
        返回分词结果,
    """
    _data = request.get_data()
    try:
        _data = json.loads(_data)
        key = _data['key']
        return jsonify(trueReturn('1111', {'data': executer.cutWords(key)}, "success"))
    except:
        return jsonify(falseReturn('0000', '', '请求失败'))

@api_blueprint.route('/wiki/<key>')
def wiki(key):
    if True:
        _wiki = Wiki.objects.filter(name = key)
        # Wiki(name='三角函数', content='<p>三角函数是基本初等函数之一，是以角度（数学上最常用弧度制，下同）为自变量，角度对应任意角终边与单位圆交点坐标或其比值为因变量的函数。</p>').save()
        if _wiki:
            wiki = _wiki[0]
        else:
            return jsonify(falseReturn('0000', '', '无此wiki'))    
        # Wiki 内容
        return jsonify(trueReturn('1111', wiki.toJson(), ''))
    else:
        return jsonify(falseReturn('000', '', '查询失败'))    


@api_blueprint.route('/graph/<key>')
def getGraphData(key):
    if True:
        return jsonify(trueReturn('1111', executer.getNodesAndRels(key), "success"))
    else:
        return jsonify(falseReturn('0000', {}, '加载错误'))


"""
Test 用作 未拿到数据前的 测试
graphtest: 返回gexf格式的演示图数据
wikitest: 返回wiki测试数据
"""

@api_blueprint.route('/graphtest')
def graphtest():
    print(request.args.get('key'))
    with open('test.gexf', 'r', encoding='UTF-8') as f:
        data = f.read()
        return Response(data, content_type="application/octet-stream")


@api_blueprint.route('/wikitest/<key>')
def wikitest(key):
    return jsonify(trueReturn('1111', {'title': '三角函数', 'content': '<p>三角函数是基本初等函数之一，是以角度（数学上最常用弧度制，下同）为自变量，角度对应任意角终边与单位圆交点坐标或其比值为因变量的函数。</p>'}, ''))
