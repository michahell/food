'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import xml.etree.ElementTree as ET

execfile('classes.py')

tree = ET.parse('database.xml')
root = tree.getroot()

# print root.tag
# print root.attrib

# def recursivePrint(node):
# 	if node is not None:
# 		print str(node.tag) + str(node.attrib) + str(node.text)
# 		for child in node:
# 			recursivePrint(child)
			
# recursivePrint(root)

bag_history_data = root[0]
vegetable_data = root[1][0]
fruit_data = root[1][1]

fruits = createOrganicThingsFrom(fruit_data, 'fruit')
vegetables = createOrganicThingsFrom(vegetable_data, 'fruit')

def createOrganicThingsFrom(organic_thing_data, type):
	for organic_thing in organic_thing_data:
		print 'creating new organic_thing obj...'
		new_fruit = OrganicThing()
		for prop in organic_thing:
			if not ET.iselement(prop):
				try:
					setattr(new_fruit, prop.tag, prop.text)
				except AttributeError:
					print 'the property ' + str(prop.tag) + ' does not exist.'
			else:
				for item in prop:
					print item.tag, item.attrib, item.text

		fruits.append(new_fruit)


# for item in bag_history:
# 	print str(node.tag) + str(node.attrib) + str(node.text)

# print '\n======\n'

# for node in vegetables:
# 	print str(node.tag) + str(node.attrib) + str(node.text)
