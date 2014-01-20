import xmltodict,json,io

def objectify(database_path)
	fileX = io.open(database_path, 'r')
	o = xmltodict.parse(fileX.read())
	my_obj = eval(json.dumps(o))
	return my_obj
	