from mongoengine import *
import datetime
from json import loads
from progressbar import *
import sys
import getopt


widgets = ['导入进度: ', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ',
           ETA(), ' ', FileTransferSpeed()]

connect('KG_Education', host='localhost', port=27017)


class Wiki(Document):
    name = StringField()
    content = StringField()
    create_date = DateTimeField(default=datetime.datetime.now())
    last_modify = DateTimeField(default=datetime.datetime.now())


def insertData(fileName):
    """inserData: 从文件将数据导入MongoDB
            filename 数据文件名
    """
    i = 0
    with open(fileName, encoding='UTF-8') as f:
        data = loads(f.read())
        print("[*]Data file loaded successfully!")
        pbar = ProgressBar(widgets=widgets, maxval=len(data)).start()
        for item in data:
            Wiki(name=item['title'], content=item['detail']).save()
            i += 1
            pbar.update(i)
        pbar.finish()
        print("[*]Data insert successfully!")
        f.close()


def help():
    """帮助"""
    helpText = """    导入工具帮助
    [options]
      -f [filename] 数据文件名, 格式为json, 包含两个元素： 'title'和'detail'
      -h help 帮助文档
"""
    print(helpText)


def main():
    opts, args = getopt.getopt(sys.argv[1:], "hf:")
    for op, value in opts:
        if op == '-f':
            insertData(value)
        elif op == '-h':
            help()
            sys.exit()
        else:
            help()


if __name__ == '__main__':
    main()
