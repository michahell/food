from operator import itemgetter

import time # Import a time module for determining the current season

# Get a product price
def get_price(product): # returns -> float
	return float(product.price)

# Check if product is often-used
def is_often_used(product): # returns -> int ( 0 / 1 )
	often = 1 if product.oftenUsed is True else 0
	return often					

# Check if a product is seasonal
def is_seasonal(product): # returns -> boolean
	seasonal = False
	# if the product has 4 seasons it is by definition not seasonal!
	if len(product.seasons) < 4:
		# check what the current month is
		month_number = time.strftime("%m")
		# check what the current season is based on the month number
		if 3 <= month_number <= 5:
			current_season = 'SPRING'
		elif 6 <= month_number <= 8:
			current_season = 'SUMMER'
		elif 9 <= month_number <= 11:
			current_season = 'AUTUMN'
		else:
			current_season = 'WINTER'
		# for all the seasons the product is available
		for season in product.seasons:
			if season == current_season:
				seasonal = True
				break

	return seasonal

# Check if a product is 'forgotten'
def is_forgotten(product): # returns -> int ( 0 / 1 )
	forgotten = 1 if product.forgotten is True else 0
	return forgotten 					

# Get a color of a product
def get_color(product): # returns -> string
	return product.color

# Get perishability level of a product
def get_perishability(product): # returns -> string
	return product.perishability

# Get locality level of a product
def get_locality(product): # returns -> string
	return product.origin

# Check if a product is easy to cook 
def get_easy_to_cook(product): # returns -> int
	return product.easyToPrepare

# Get the number of pieces for a product
def get_piece_size(product): # returns -> int
	return product.pieces

# Remove an item (bag object) by its name
def removeItemByName(name, items):
	for i in items:
		if i.name == name:
			items.remove(i)

# Get the 5 best bags in order of decreasing grading score
def getBestBags(bags, ordering, n):
	backupBags = list(bags)
	backupOrdering = list(ordering)
	best_bags = []
	for k in range(min(n, len(bags))):
		index_max = -1
		maximum = -1
		for i in range(len(backupOrdering)):
			if backupOrdering[i] > maximum:
				maximum = backupOrdering[i]
				index_max = i
		best_bags.append(backupBags[index_max])
		backupBags.remove(backupBags[index_max])
		backupOrdering.pop(index_max)
	return best_bags
