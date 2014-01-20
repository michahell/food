'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import json

execfile('classes.py')

def create_previous_bags(data):
	previous_bags = []
	print data
	return previous_bags

def create_organic_things(ot_type, data):
	organic_things = []
	for ot in data:
		# print '\n', ot, '\n'
		new_ot = OrganicThing()
		for prop in ot:
			value = ot[prop]
			# print prop, value
			try:
				setattr(new_ot, prop, value)
			except AttributeError:
				print 'the property ' + str(prop) + ' does not exist.'
		new_ot.category = ot_type
		organic_things.append(new_ot)
	return organic_things


json_data = open('data.json').read()
db = json.loads(json_data)

# previous_bags = create_previous_bags(db['foodDatabase']['baghistory'])

def get_all_fruits():
	return create_organic_things('fruit', db['foodDatabase']['food']['fruits']['fruit'])

def get_all_vegetables():
	return create_organic_things('vegetable', db['foodDatabase']['food']['vegetables']['vegetable'])

