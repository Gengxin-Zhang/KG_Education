with open('entityRelation_raw.json','r',encoding='UTF-8') as file:
	data=file.read().split('\n')
	data=list(set(data))
	with open('entityRelation.json','w',encoding='UTF-8') as file1:
		for d in data:
			file1.write(d)
			file1.write('\n')