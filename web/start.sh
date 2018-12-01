# 拉取 neo4j 镜像 并 运行
docker pull neo4j
docker run -p=7474:7474 -p=7687:7687 -d --ENV=NEO4J_AUTH=neo4j/123456 neo4j
# 构建 KG_Education Docker 镜像 并 运行
docker build -t "kgeducation" .
docker container run --name kgeducation01 --rm -d -it -p 9090:9090 kgeducation