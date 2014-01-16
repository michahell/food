'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

import optparse
import xml.etree.ElementTree as ET


'''
TODO:

Find and use XML library or python default if possible

- convert all XML data into temp. python dict objects for use in script
- find out how to write to xml database

- function to generate all possible bags
- function (general) to apply a rule

'''


'''
PSEUDO CODE:
'''


parser = optparse.OptionParser()
parser.add_option("-t", help="some help text")

(option, args) = parser.parse_args()

print "t = " + str(option.t)