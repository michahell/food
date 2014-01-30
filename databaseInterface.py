'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

''' This file implements the interface of the database, providing all the functions to interact with it''' 

import xmltodict,json,io 	# in case xmltodict is not installed: "sudo pip install xmltodict"

from classes import OrganicThing, Bag, Recipe

############################# INTERNAL FUNCTINOS ###############################

# returns the entire database as a Python dictionary
def objectifyWholeDB(database_path):
	fileX = io.open(database_path, 'r') # open the database xml file
	o = xmltodict.parse(fileX.read()) 	# parse the xml
	my_obj = eval(json.dumps(o)) 		# translate from tree to dict
	return my_obj

# add to an item all the recipes in which it appears 
def addRecipes(item):
	recipes = get_all_recipes()					# get all recipes from the database
	for r in recipes:							# for each recipe
		if item.name in r.ingredients:			#	if it contains the item
			item.recipes.append(r.name)			# 		the recipe is added to the item's list of recipes
	recipes = get_all_xmas_recipes()			# same for the Christmas recipes
	for r in recipes:
		if item.name in r.ingredients:
			item.xmasRecipes.append(r.name)

# creates an object of type OrganicThing from a simple dictionary representing a vegetable
def create_vegetable(v):
	new_vegetable = OrganicThing()
	new_vegetable.name = v['name']
	new_vegetable.category = 'vegetable'
	new_vegetable.price = float(v['price'])		# the price read from the database as a string,
												# so it has to be converted
	new_vegetable.pieces = v['pieces']
	seasons = []
	for s in v['seasons']['season']:
		seasons.append(s)
	new_vegetable.seasons = seasons
	new_vegetable.origin = v['origin']
	new_vegetable.easyToPrepare = v['easyToPrepare']  == 'yes' # string to boolean
	new_vegetable.color = v['color']
	new_vegetable.perishability = v['perishability']
	new_vegetable.oftenUsed = v['oftenUsed']  == 'yes' 			# string to boolean
	new_vegetable.forgotten = v['forgotten']  == 'yes' 			# string to boolean
	addRecipes(new_vegetable)	# call the function for adding all the recipes to the item
	return new_vegetable

# creates an object of type OrganicThing from a simple dictionary representing a fruit 
def create_fruit(f):
	new_fruit = OrganicThing()
	new_fruit.name = f['name']
	new_fruit.category = 'fruit'
	new_fruit.price = float(f['price'])			# the price read from the database as a string,
												# so it has to be converted
	new_fruit.pieces = f['pieces']
	seasons = []
	for s in f['seasons']['season']:
		seasons.append(s)
	new_fruit.seasons = seasons
	new_fruit.origin = f['origin']
	new_fruit.easyToPrepare = f['easyToPrepare'] == 'yes'	# string to boolean
	new_fruit.color = f['color']
	new_fruit.perishability = f['perishability']
	new_fruit.oftenUsed = None	# fruits have no value for this field
	new_fruit.forgotten = None	# fruits have no value for this field
	addRecipes(new_fruit)	# call the function for adding all the recipes to the item
	return new_fruit

# serach for a fruit in the database given its name. Returns it as a dict
def get_fruit_by_name(strFruit):
	whole = objectifyWholeDB('database.xml')
	fruits = whole['foodDatabase']['food']['fruits']['fruit']
	for f in fruits:
		if f['name'] == strFruit:
			return f
	return None

# serach for a vegetable in the database given its name. Returns it as a dict
def get_vegetable_by_name(strVegetable):
	whole = objectifyWholeDB('database.xml')
	vegs = whole['foodDatabase']['food']['vegetables']['vegetable']
	for v in vegs:
		if v['name'] == strVegetable:
			return v
	return None

# translates a Bag into a dict
def prepareBagForConversion(bag):
	modifiedBag = {}
	modifiedBag['foodItems'] = {}
	modifiedBag['foodItems']['fruitItem'] = bag.fruit.name
	vegetables = []
	for i in range(len(bag.vegetables)):
		vegetables.append(bag.vegetables[i].name)
	modifiedBag['foodItems']['vegetableItem'] = vegetables
	modifiedBag['price'] = bag.price
	return modifiedBag


############################# FUNCTINOS THAT ARE CALLED FROM EXTERNAL MODULES ###############################

# reads all fruits from database and returns them as a list or OrganicThing
def get_all_fruits():
	whole = objectifyWholeDB('database.xml')	# get the whole database as a Python dict
	fruitsDict = whole['foodDatabase']['food']['fruits']['fruit'] # select only the fruits
	fruits = []
	for f in fruitsDict:			# for each fruit
		new_fruit=create_fruit(f)	#	create the relative OrganicThing
		fruits.append(new_fruit)	#	append it to the list
	return fruits

# reads all vegetables from database and returns them as a list or OrganicThing
def get_all_vegetables():
	whole = objectifyWholeDB('database.xml')	# get the whole database as a Python dict
	vegetablesDict = whole['foodDatabase']['food']['vegetables']['vegetable'] # select only the vegetables
	vegetables = []
	for v in vegetablesDict:				# for each vegetable
		new_vegetable=create_vegetable(v)	#	create the relative OrganicThing
		vegetables.append(new_vegetable)	#	append it to the list
	return vegetables

# reads the most recent bag from database and returns it as a Bag
def get_previous_bag():
	whole = objectifyWholeDB('database.xml')	# get the whole database as a Python dict
	bagDict = whole['foodDatabase']['baghistory']['bag'][0] # selects only the last bag (it is always the most recent)
	bag = Bag()
	bag.price = float(bagDict['price'])			# the price read from the database as a string,
												# so it has to be converted
	strFruit = bagDict['foodItems']['fruitItem']
	completeFruit = get_fruit_by_name(strFruit)	# the bag contains only the name of the fruit but the entire entity
												# is here needed
	bag.fruit =create_fruit(completeFruit)
	vegetables = []
	for v in bagDict['foodItems']['vegetableItem']:
		completeVegetable=get_vegetable_by_name(v)		# the bag contains only the name of the vegetables but the entire
														# entities are here needed
		vegetable=create_vegetable(completeVegetable)
		vegetables.append(vegetable)
	bag.vegetables = vegetables
	return bag

# reads all normal recipes from database and returns them as a list of Recipe
def get_all_recipes():
	whole = objectifyWholeDB('database.xml')	# get the whole database as a Python dict
	repicesDict = whole['foodDatabase']['recipes']['recipe'] # selects only the normal recipes
	recipes = []
	for r in repicesDict:
		new_recipe = Recipe()
		new_recipe.name = r['name']
		new_recipe.description = r['description']
		for ingredient in r['ingredient']:
			new_recipe.ingredients.append(ingredient)
		recipes.append(new_recipe)
	return recipes

# reads all Christmas recipes from database and returns them as a list of Recipe
def get_all_xmas_recipes():
	whole = objectifyWholeDB('database.xml')	# get the whole database as a Python dict
	repicesDict = whole['foodDatabase']['xMasRecipes']['recipe'] # selects only the Christmas recipes
	recipes = []
	for r in repicesDict:
		new_recipe = Recipe()
		new_recipe.name = r['name']
		new_recipe.description = r['description']
		for ingredient in r['ingredient']:
			new_recipe.ingredients.append(ingredient)
		recipes.append(new_recipe)
	return recipes

# inserts a new bag into the database as first bag item
def addNewBagIntoDatabase(bag):
	modifiedBag = prepareBagForConversion(bag)		# the bag is given in input as an Object and it has to be
													# translated into a dict in order to be translated into XML
													# using the library xmltodict
	newDatabaseDict = objectifyWholeDB('database.xml') 	# read database
	newDatabaseDict['foodDatabase']['baghistory']['bag'].insert(0, modifiedBag) # insert as first
	newDatabaseXML = xmltodict.unparse(newDatabaseDict)
	databaseFile = open("database.xml", "w") 			# rewrite updated database
	databaseFile.write(newDatabaseXML)
	databaseFile.close()
