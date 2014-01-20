'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

from xml_objectifier import xml2obj
# see: http://code.activestate.com/recipes/534109-xml-to-python-data-structure/

food = xml2obj(open('database.xml'))

# print len(food.baghistory)
# print food.baghistory

