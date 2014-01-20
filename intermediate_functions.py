
import time


def get_price(product):
	return float(product.price)

def is_seasonal(product):
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

def is_forgotten(product):
	return 1 if product.forgotten == 'yes' else 0

def get_color(product):
	return product.color

# get_perishability(product) -> int/string
# get_locality(product) -> int/string
# get_easy_to_cook(product) -> int/string
# get_piece_size(product) ->int/string
# get_color(product) -> string
