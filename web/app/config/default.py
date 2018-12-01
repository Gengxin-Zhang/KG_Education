import os
import json

class Config():
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 9090
    HTML_MINIFY = True
    SECRET_KEY = 'EG_Education_development_key'
    MONGODB_SETTINGS = {
        'db': 'KG_Education',
        'host': '127.0.0.1',
        'port': 27017,
    }
    