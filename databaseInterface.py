import xmltodict,json,io

def objectify(database_path)
	fileX = io.open(database_path, 'r')
	o = xmltodict.parse(fileX.read())
	my_obj = eval(json.dumps(o))
	return my_obj
	

def get_all_fruits():
	return fruits

def get_all_vegetables():
	return vegetables

def get_previous_bag():
	return previous_bag