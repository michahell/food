import xmltodict,json,io

from classes import OrganicThing, Bag, Recipe

def objectifyWholeDB(database_path):
	fileX = io.open(database_path, 'r')
	o = xmltodict.parse(fileX.read())
	my_obj = eval(json.dumps(o))
	return my_obj['foodDatabase']

def addRecipes(item):
	recipes = get_all_recipes()
	for r in recipes:
		if item.name in r.ingredients:
			item.recipes.append(r.name)
	recipes = get_all_xmas_recipes()
	for r in recipes:
		if item.name in r.ingredients:
			item.xmasRecipes.append(r.name)

def create_vegetable(v):
	new_vegetable = OrganicThing()
        new_vegetable.name = v['name']
        new_vegetable.category = 'vegetable'
        new_vegetable.price = float(v['price'])
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
        addRecipes(new_vegetable)
	return new_vegetable

def create_fruit(f):
	new_fruit = OrganicThing()
	new_fruit.name = f['name']
	new_fruit.category = 'fruit'
	new_fruit.price = float(f['price'])
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
	addRecipes(new_fruit)
	return new_fruit

def get_fruit_by_name(strFruit):
	whole = objectifyWholeDB('database.xml')
	fruits = whole['food']['fruits']['fruit']
	for f in fruits:
		if f['name'] == strFruit:
			return f
	return None

def get_vegetable_by_name(strVegetable):
	whole = objectifyWholeDB('database.xml')
	vegs = whole['food']['vegetables']['vegetable']
	for v in vegs:
		if v['name'] == strVegetable:
			return v
	return None

############################################################

def get_all_fruits():
	whole = objectifyWholeDB('database.xml')
	fruitsDict = whole['food']['fruits']['fruit']
	fruits = []
	for f in fruitsDict:
		new_fruit=create_fruit(f)
		fruits.append(new_fruit)
	return fruits

def get_all_vegetables():
	whole = objectifyWholeDB('database.xml')
	vegetablesDict = whole['food']['vegetables']['vegetable']
	vegetables = []
	for v in vegetablesDict:
		new_vegetable=create_vegetable(v)
		vegetables.append(new_vegetable)
	return vegetables

def get_previous_bag():
	whole = objectifyWholeDB('database.xml')
	bagDict = whole['baghistory']['bag'][0]
	bag = Bag()
	bag.price = float(bagDict['price'])

	strFruit = bagDict['foodItems']['fruitItem']
	completeFruit = get_fruit_by_name(strFruit)
	bag.fruit =create_fruit(completeFruit)

	vegetables = []
	for v in bagDict['foodItems']['vegetableItem']:
		completeVegetable=get_vegetable_by_name(v)
		vegetable=create_vegetable(completeVegetable)
		vegetables.append(vegetable)
	bag.vegetables = vegetables
	return bag

def get_all_recipes():
	whole = objectifyWholeDB('database.xml')
	repicesDict = whole['recipes']['recipe']
	recipes = []
	for r in repicesDict:
		new_recipe = Recipe()
		new_recipe.name = r['name']
		new_recipe.description = r['description']
		for ingredient in r['ingredient']:
			new_recipe.ingredients.append(ingredient)
		recipes.append(new_recipe)
	return recipes

def get_all_xmas_recipes():
	whole = objectifyWholeDB('database.xml')
	repicesDict = whole['xMasRecipes']['recipe']
	recipes = []
	for r in repicesDict:
		new_recipe = Recipe()
		new_recipe.name = r['name']
		new_recipe.description = r['description']
		for ingredient in r['ingredient']:
			new_recipe.ingredients.append(ingredient)
		recipes.append(new_recipe)
	return recipes
