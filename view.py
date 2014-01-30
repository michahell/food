'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

''' This file implements the user interface '''

execfile('controller.py') # Use the functionality of controller.py

# Print the bag contents on the terminal screen
def print_bag(bag):
	s=""
	for item in bag.vegetables:
		s+=item.name + ","
	s+=bag.fruit.name
	print s

#################### Main program #################################################################

# Ask the user to choose a bag type
bag_type=raw_input("\nDear customer, \nWelcome to the f00d KBS. \n\nPlease select the type of bag (enter 0 or 1):\n0 - Normal bag\n1 - Christmas special bag\n")

bag_type=int(bag_type)
bags=create_configurations(bag_type) # Call the controller function to create optimal configurations

print "Final set of bags:\n"

count=1
for b in bags:
	s=str(count) + " - "
	print s
	print_bag(b)
	count+=1

# Ask the user the choose a bag from the offered few
chosen_bag=raw_input("\nPlease select your bag (enter 1-5):")
addNewBag(bags[int(chosen_bag)-1]) # Add the bag to the db and notify the user
print "\nYou chose bag number " + chosen_bag + "! This bag is stored in the database."

