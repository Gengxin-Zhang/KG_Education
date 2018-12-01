def trueReturn(code, data, msg):
    """ trueReturn: 返回正确的查询
    """
    return {
        "code" : code,
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(code ,data, msg):
    """ falseReturn: 返回查询错误
    """
    return {
        "code" : code,
        "status": False,
        "data": data,
        "msg": msg
    }