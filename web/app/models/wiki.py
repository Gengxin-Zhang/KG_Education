from flask_mongoengine import MongoEngine
import types
import time
from app import db
from datetime import datetime
from hashlib import md5

allowAttrType = (
    int,
    str,
    bool,
    datetime,
)

notShowKey = (
    '_Document__objects',
    'STRICT',
    '__module__',
    '_auto_id_field',
    '_class_name',
    '_cls',
    '_created',
    '_dynamic',
    '_dynamic_lock',
    '_initialised',
    '_is_base_cls',
    '_is_document',

)


def toMd5(s):
    """ toMd5: 获取字符串md5
        s string
        return 字符串的md5
    """
    return md5(s.encode('utf-8')).hexdigest()


def toJson(Data):
    """toJson: 获取该表所有字段, 判断类型是否包含在 allowAttrType, 将字段格式化为json
        Data MongoEngine.Document类
        return 返回json格式化后的字段数据
    """
    _json = {}
    for key in dir(Data):
        if key in notShowKey:
            continue
        value = getattr(Data, key)
        if isinstance(value, allowAttrType) \
                and isinstance(key, allowAttrType):
            # 如果属性为datetime类型,转换为时间戳
            if isinstance(key, datetime):
                _json[key] = time.mktime(value.timetuple())*1000
            else:
                # 其他类型直接转换
                _json[key] = value
    return _json


class Wiki(db.Document):
    name = db.StringField()
    content = db.StringField()
    create_date = db.DateTimeField(default=datetime.now())
    last_modify = db.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
    
    def toJson(self):
        return toJson(self)


class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    email = db.StringField()
    used = db.BooleanField(default=False)
    code = db.StringField()
    create_time = db.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    def checkPassword(self, _password):
        """ checkPassword: 验证密码是否正确
            _password 需要验证的密码
            return 密码是否正确
        """
        if toMd5(_password) == self.password:
            return True
        return False

    def changePassword(self, newPassword):
        """ changePassword: 修改用户密码
            newPassword 新密码
        """
        self.password = toMd5(newPassword)
        self.save()
    
    def toJson(self):
        return toJson(self)