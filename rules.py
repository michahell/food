'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import itertools

execfile('databaseInterface.py')
execfile('utilities.py')

number_of_products = 5
best_bags_count=5

##############################################################################################################

def generate_all_possible_bags(): # generate all the possible bags of 4 vegetables and 1 fruit which don't contain items from the previous week

	fruits = get_all_fruits()
	vegetables = get_all_vegetables()
	last_bag = get_previous_bag()

	last_fruit=last_bag.fruit
	removeItemByName(last_fruit,fruits)

	last_vegetables=last_bag.vegetables
	for item in last_vegetables: # This for loop is used to remove the fruits and the vegetables from the previous week from the current collections of possible items
		removeItemByName(item,vegetables)
	
	### Generate all the possible crates with 4 vegetables and 1 fruit

	bags = []
	vegetable_combinations = itertools.combinations(vegetables, 4)
	for vc in vegetable_combinations:
		for f in fruits:
			newbag = [f]
			for product in vc:
				newbag.append(product)
			bags.append(newbag)
	return bags

##############################################################################################################

def apply_compulsory(bags): # apply the compulsory rules to filter the invalid bags
	for bag in bags: # check the price constraint
		price = get_bag_price(bag)
		if price > 5 or price < 4:
			bags.remove(bag)
	return bags

##############################################################################################################

def apply_selection(bags): # apply the selection rules to filter the bags further if possible
	bags_length=len(bags)
	quality_counter = [0] * bags_length
	weight_season = 0.6
	weight_forget = 0.4
	
	# Seasonal rule
	count=0
	for bag in bags:
		quality_counter[count] = get_seasonal_products_count(bag) * weight_season
		count += 1
	
	maximum=max(quality_counter)

	# Forgetfulness rule
	count=0
	for bag in bags:
		if is_forgotten_bag(bag):
			quality_counter[count] += maximum * weight_forget
		count += 1

	# Get the new (updated) bags subset
	new_bags = []
	overall_max = max(quality_counter)
	for count in xrange(0,len(bags)):
		if overall_max - quality_counter[count] < 2.0: # if the bag is sufficiently close to the optimal one, add it to the selected subset
			new_bags.append(bags[count])

	return new_bags

##############################################################################################################

def apply_preferences(bags): # apply the preference rules to order the bag collection
	ordering_number=[0] * len(bags)
	weight_high = 0.6
	weight_medium = 0.25
	weight_low = 0.15
	count=0

	# Use the preference rules
	for bag in bags:
		ordering_number[count] = \
		weight_high * (get_locality_count(bag) / 20 + get_perishability_count(bag) / 15) + \
		weight_medium * (get_easy_to_cook_count(bag) / 5) + \
		weight_low * (number_of_products / get_piece_size_count(bag) + get_color_count(bag) / number_of_products)

	# Order the bags based on their 'ordering_number' value
	bags = getBestBags(bags, ordering_number, best_bags_count)

	return bags

##################################### END OF THE MAIN FUNCTIONS ##############################################

def get_bag_price(bag):
	overall_price=0.0
	for item in bag:
		overall_price+=float(get_price(item))
	return overall_price

def is_forgotten_bag(bag):
	forgotten_count=0
	for item in bag:
		forgotten_count+=is_forgotten(item)
	if 1<=forgotten_count<=2:
		return True
	else:
		return False

def get_seasonal_products_count(bag):
	seasonal_count = 0
	for item in bag:
		if is_seasonal(item):
			seasonal_count += 1
	return seasonal_count

def get_locality_count(bag):
	locality_count=0
	for item in bag:
		loc=get_locality(item)
		if loc=='REGIONAL':
			loc_coef=4
		elif loc=='NATIONAL':
			loc_coef=3
		elif loc=='EUROPEAN':
			loc_coef=2
		else:
			loc_coef=1
		locality_count+=loc_coef
	return locality_count

def get_perishability_count(bag):
	perish_count=0
	for item in bag:
		per=get_perishability(item)
		if per=='SLOW':
			per_coef=3
		elif per=='NORMAL':
			per_coef=2
		else: # 'FAST'
			per_coef=1
		perish_count+=per_coef
	return perish_count

def get_easy_to_cook_count(bag):
	easy_count=0
	for item in bag:
		easy_count+=get_easy_to_cook(item)
	return easy_count

def get_piece_size_count(bag):
	pieces_count=0
	for item in bag:
		pieces_count+=int(get_piece_size(item))
	return pieces_count

def get_color_count(bag):
	colors=[]
	for item in bag:
		c=get_color(item)
		if c not in colors:
			colors.append(c)
	return len(colors)
