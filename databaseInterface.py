import xmltodict,json,io

from classes import OrganicThing, Bag

def objectifyWholeDB(database_path):
	fileX = io.open(database_path, 'r')
	o = xmltodict.parse(fileX.read())
	my_obj = eval(json.dumps(o))
	return my_obj['foodDatabase']
	
def get_all_fruits():
	whole = objectifyWholeDB('database.xml')
	fruitsDict = whole['food']['fruits']['fruit']
	fruits = []
	for f in fruitsDict:
		new_fruit = OrganicThing()
		new_fruit.name = f['name']
		new_fruit.category = 'fruit'
		new_fruit.price = f['price']
		new_fruit.pieces = f['pieces']
		seasons = []
		for s in f['seasons']['season']:
			seasons.append(s)
		new_fruit.seasons = seasons
		new_fruit.origin = f['origin']
		new_fruit.easyToPrepare = f['easyToPrepare'] == 'yes'
		new_fruit.color = f['color']
		new_fruit.perishability = f['perishability']
		new_fruit.oftenUsed = None
		new_fruit.forgotten = None
		fruits.append(new_fruit)
	return fruits


def get_all_vegetables():
	whole = objectifyWholeDB('database.xml')
	vegetablesDict = whole['food']['vegetables']['vegetable']
	vegetables = []
	for v in vegetablesDict:
		new_vegetable = OrganicThing()
		new_vegetable.name = v['name']
		new_vegetable.category = 'fruit'
		new_vegetable.price = v['price']
		new_vegetable.pieces = v['pieces']
		seasons = []
		for s in v['seasons']['season']:
			seasons.append(s)
		new_vegetable.seasons = seasons
		new_vegetable.origin = v['origin']
		new_vegetable.easyToPrepare = v['easyToPrepare']  == 'yes'
		new_vegetable.color = v['color']
		new_vegetable.perishability = v['perishability']
		new_vegetable.oftenUsed = v['oftenUsed']  == 'yes'
		new_vegetable.forgotten = v['forgotten']  == 'yes'
		vegetables.append(new_vegetable)
	return vegetables

def get_previous_bag():
	whole = objectifyWholeDB('database.xml')
	bagDict = whole['baghistory']['bag'][0]
	bag = Bag()
	bag.price = bagDict['price']
	bag.fruit = bagDict['foodItems']['fruitItem']
	vegetables = []
	for v in bagDict['foodItems']['vegetableItem']:
		vegetables.append(v)
	bag.vegetables = vegetables
	return bag

