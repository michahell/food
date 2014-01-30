'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import itertools

execfile('databaseInterface.py')
execfile('helperFunctions.py')

number_of_products = 5
best_bags_count=5

##############################################################################################################

def generate_all_possible_bags(bag_type): # generate all the possible bags of 4 vegetables and 1 fruit which don't contain items from the previous week

	fruits = get_all_fruits()
	vegetables = get_all_vegetables()

	if bag_type==0: # if the bag is normal, take into account the previous bag
		last_bag = get_previous_bag()
		last_fruit=last_bag.fruit
		removeItemByName(last_fruit.name,fruits)
		last_vegetables=last_bag.vegetables
		for item in last_vegetables: # This for loop is used to remove the fruits and the vegetables from the previous week from the current collections of possible items
			removeItemByName(item.name,vegetables)
	
	### Generate all the possible crates with 4 vegetables and 1 fruit

	bags = []
	vegetable_combinations = itertools.combinations(vegetables, 4)
	for vc in vegetable_combinations:
		for f in fruits:
			newbag=Bag()
			newbag.fruit=f
			newbag.vegetables=[]
			for product in vc:
				newbag.vegetables.append(product)
			newbag.price=get_bag_price(vc,f)
			bags.append(newbag)
	return bags

##############################################################################################################

def apply_compulsory(bags): # apply the compulsory rules to filter the invalid bags
	for bag in bags: # check the price constraint
		if bag.price > 5 or bag.price < 4:
			bags.remove(bag)
	return bags

##############################################################################################################

def apply_selection(bags): # apply the selection rules to filter the bags further if possible
	bags_length=len(bags)
	quality_counter = [0] * bags_length
	weight_often_used = 0.5
	weight_season = 0.3
	weight_forget = 0.2

	# Seasonal rule
	count=0
	for bag in bags:
		quality_counter[count] = get_seasonal_products_count(bag) * weight_season
		count += 1	
	maximum=max(quality_counter)

	count=0
	for bag in bags:
                quality_counter[count] /= maximum
                count += 1

	# Often used rule
	count=0
        for bag in bags:
                quality_counter[count] += get_often_used_count(bag) * weight_often_used
                count += 1


	# Forgetfulness rule
	count=0
	for bag in bags:
		if is_forgotten_bag(bag):
			quality_counter[count] += 1 * weight_forget
		count += 1

	# Get the new (updated) bags subset
	new_bags = []
	overall_max = max(quality_counter)
	for count in xrange(0,len(bags)):
		if overall_max - quality_counter[count] < 0.2: # if the bag is sufficiently close to the optimal one, add it to the selected subset
			new_bags.append(bags[count])

	return new_bags

##############################################################################################################

def apply_preferences(bags,bag_type): # apply the preference rules to order the bag collection
	ordering_number=[0] * len(bags)
	weight_high = 0.6
	weight_medium = 0.25
	weight_low = 0.15
	count=0

	# Use the preference rules
	if bag_type==0: # normal bag
		for bag in bags:	
			ordering_number[count] = \
			weight_high * (get_locality_count(bag) / (4*number_of_products) + get_perishability_count(bag)/(3*number_of_products) + get_recipe_score(bag)) + \
			weight_medium * (get_easy_to_cook_count(bag) / number_of_products) + \
			weight_low * (number_of_products / get_piece_size_count(bag) + get_color_count(bag) / number_of_products)
	else: # christmas bag -> use only recipes, color and pieces
		for bag in bags:	
			ordering_number[count] = \
			weight_high * ( get_xmas_recipe_score(bag) ) + weight_low * (number_of_products / get_piece_size_count(bag) + get_color_count(bag) / number_of_products)


	# Order the bags based on their 'ordering_number' value
	bags = getBestBags(bags, ordering_number, best_bags_count)

	return bags

##################################### END OF THE MAIN FUNCTIONS ##############################################

def get_bag_price(vegetables,fruit):
	overall_price=0.0
	for item in vegetables:
		overall_price+=get_price(item)
	overall_price+=fruit.price
	return overall_price

def get_often_used_count(bag):
        often_count = 0
        for item in bag.vegetables:
                if is_often_used(item):
                        often_count += 1
	if is_often_used(bag.fruit):
		often_count+=1
	return 1/(1+abs(often_count-1))


def is_forgotten_bag(bag):
	forgotten_count=0
	for item in bag.vegetables:
		forgotten_count+=is_forgotten(item)
	if 1<=forgotten_count<=2:
		return True
	else:
		return False

def get_seasonal_products_count(bag):
	seasonal_count = 0
	for item in bag.vegetables:
		if is_seasonal(item):
			seasonal_count += 1
	return seasonal_count

def get_recipe_score(bag):
	score=0.0
 	for veg in bag.vegetables:
		score+=len(veg.recipes)
	if score != 0.0:
		score = 1-1/score
	return score

def get_xmas_recipe_score(bag):
	score=0.0
 	for veg in bag.vegetables:
		score+=len(veg.xmasRecipes)
	if score != 0.0:
		score = 1-1/score
	return score

def get_locality_count(bag):
	locality_count=0
	for item in bag.vegetables:
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
	loc=get_locality(bag.fruit)
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
	for item in bag.vegetables:
		per=get_perishability(item)
		if per=='SLOW':
			per_coef=3
		elif per=='NORMAL':
			per_coef=2
		else: # 'FAST'
			per_coef=1
		perish_count+=per_coef
	per=get_perishability(bag.fruit)
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
	for item in bag.vegetables:
		easy_count+=get_easy_to_cook(item)
	easy_count+=get_easy_to_cook(bag.fruit)
	return easy_count

def get_piece_size_count(bag):
	pieces_count=0
	for item in bag.vegetables:
		pieces_count+=int(get_piece_size(item))
	pieces_count+=int(get_piece_size(bag.fruit))
	return pieces_count

def get_color_count(bag):
	colors=[]
	for item in bag.vegetables:
		c=get_color(item)
		if c not in colors:
			colors.append(c)
	c=get_color(bag.fruit)
	if c not in colors:
		colors.append(c)
	return len(colors)
