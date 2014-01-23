'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

execfile('controller.py')

def print_bag(bag):
	s=""
	for item in b.vegetables:
		s+=item.name + ","
	s+=b.fruit.name
	print s

bag_type=raw_input("\nDear customer, \nWelcome to the f00d KBS. \n\nPlease select the type of bag (enter 0 or 1):\n0 - Normal bag\n1 - Christmas special bag\n")

bag_type=int(bag_type)
bags=create_configurations(bag_type)

print "Final set of bags:\n"

count=1
for b in bags:
	s=str(count) + " - "
	print s
	print_bag(b)
	count+=1

chosen_bag=raw_input("\nPlease select your bag (enter 1-5):")
print "\nYou chose " + chosen_bag # TODO: Instead of this, insert the new bag in the DB!!!
