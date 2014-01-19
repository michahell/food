'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import json

execfile('classes.py')


def createOrganicThings(ot_type, source):
	organicThings = []
	for ot in source:
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
		organicThings.append(new_ot)
	return organicThings


json_data = open('data.json').read()
db = json.loads(json_data)

fruits = createOrganicThings('fruit', db['foodDatabase']['food']['fruits']['fruit'])
vegetables = createOrganicThings('vegetable', db['foodDatabase']['food']['vegetables']['vegetable'])

for fruit in fruits:
	print fruit

for vegetable in vegetables:
	print vegetable