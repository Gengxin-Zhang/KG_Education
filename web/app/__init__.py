from flask import Flask, request, render_template, g
from htmlmin import minify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(offline=False) -> Flask:
    flask_app = Flask(__name__,
                static_folder='../frontend/dist/static',
                template_folder='../frontend/dist')
    
    """ 根据环境变量载入Config """
    from app.config import get_config
    _get_config = get_config()
    flask_app.config.from_object(_get_config)

    """flask上下文"""
    ctx = flask_app.app_context()
    ctx.push()
    
    """设置Flask允许跨域访问"""
    CORS(flask_app, supports_credentials=True)

    """导入并注册 Blueprint"""
    from app.api.views import api_blueprint
    flask_app.register_blueprint(api_blueprint, url_prefix = '/api')
    
    """初始化Mongodb数据库"""
    db.init_app(flask_app)
    
    """处理所有请求"""
    @flask_app.route('/', defaults={'path': ''})
    @flask_app.route('/<path:path>')
    def catch_all(path):
        return render_template('index.html')

    # """用 htmlmin 压缩 HTML，减轻带宽压力"""
    # @app.after_request
    # def response_minify(response):
    #     if app.config['HTML_MINIFY'] and response.content_type == u'text/html; charset=utf-8':
    #         response.set_data(minify(response.get_data(as_text=True)))
    #     return response

    return flask_app