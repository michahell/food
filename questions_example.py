

# =======================================

def get_bag_price(vegetables,fruit):
	overall_price=0.0
	for item in vegetables:
		overall_price+=get_price(item)
	overall_price+=fruit.price
	return overall_price

def get_configuration_price(configuration):
	overall_price = 0.0
	for item in configuration:
		overall_price += item.price
	return overall_price

# =======================================