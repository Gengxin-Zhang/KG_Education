# 数据   
  
如需要导入数据，请将数据放置于neo4j安装目录下的import文件夹中，并按照顺序在neo4j控制台中执行以下CQL语句：
  
```
    LOAD CSV WITH HEADERS FROM "file:///data_with_detail.csv" AS line  
    MERGE (a:Item{title:line.title,url:line.url,context:line.detail}) return a  
  
    LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line  
    MERGE (a:NewItem{title:line.title}) return a  

    LOAD CSV WITH HEADERS FROM "file:///wikidata_relation.csv" AS line  
    MATCH (f:Item{title:line.Item1}),(t:Item{title:line.Item2})  
    MERGE (f)-[a:rel{property:line.relation}]->(t) return a  

    LOAD CSV WITH HEADERS FROM "file:///wikidata_relation2.csv" AS line  
    MATCH (f:Item{title:line.Item}),(t:NewItem{title:line.NewNode})  
    MERGE (f)-[a:rel{property:line.relation}]->(t) return a  
```  

**由于数据量较大，初次导入数据需要较长时间，请耐心等候**