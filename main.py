'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

execfile('parser.py')
execfile('functions.py')

# parser = optparse.OptionParser()
# parser.add_option("-t", help="some help text")

# (option, args) = parser.parse_args()

# print "t = " + str(option.t)

bags=generate_all_possible_bags() # generate all the possible bags of 4 vegetables and 1 fruit which don't contain items from the previous week
bags=apply_compulsory(bags) # apply the compulsory rules to filter the invalid bags
bags=apply_selection(bags) # apply the selection rules to filter the bags further if possible
bags=apply_preferences(bags) # apply the preference rules to order the bag collection
