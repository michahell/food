from operator import itemgetter

import time

def get_price(product):
	return float(product.price)

def is_often_used(product): # returns -> int ( 0 / 1 )
	often = 1 if product.oftenUsed is True else 0
	return often					

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

def check_overlapping(bag,recipe):
	overlap_count=0
	for item in bag.vegetables:
		if item in recipe.ingredients:
			overlap_count+=1
	return overlap_count		

def is_forgotten(product): # returns -> int ( 0 / 1 )
	forgotten = 1 if product.forgotten is True else 0
	return forgotten 					

def get_color(product): # returns -> string
	return product.color

def get_perishability(product): # returns -> string
	return product.perishability

def get_locality(product): # returns -> string
	return product.origin

def get_easy_to_cook(product): # returns -> int
	return product.easyToPrepare

def get_piece_size(product): # returns -> int
	return product.pieces

def removeItemByName(name, items):
	for i in items:
		if i.name == name:
			items.remove(i)

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
