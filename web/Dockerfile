FROM ubuntu:16.04

MAINTAINER Zhangone zhgx3ng@outlook.com

WORKDIR /var/www/KG_Education

# 更新软件
# 安装 Python3及相关依赖, mongodb
RUN apt update && apt install -y python3 python3-dev python3-pip mongodb

# 把代码加入镜像中
COPY . .

# 安装Python依赖库
RUN pip3 install -r requirements.txt

#导入数据
RUN python3 ./tools/importData.py -n ./tools/data.json

EXPOSE 9090

# 运行uwsgi
CMD ["uwsgi", "--ini", "/var/www/KG_Education/uwsgi.ini"]