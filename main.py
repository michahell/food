'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

execfile('rules.py')

bags=generate_all_possible_bags() # generate all the possible bags of 4 vegetables and 1 fruit which don't contain items from the previous week
print "Initial set of possible bags:" + str(len(bags))
bags=apply_compulsory(bags) # apply the compulsory rules to filter the invalid bags
print "Set of valid bags: " + str(len(bags))
bags=apply_selection(bags) # apply the selection rules to filter the bags further if possible
print "Set of selected bags:" +  str(len(bags))
bags=apply_preferences(bags) # apply the preference rules to order the bag collection
print "Ordered set of optimal bags:" + str(len(bags))
for b in bags:
        s=""
        for item in b:
                s+=item.name + ","
        print s
