'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

''' This file defines all the classes of the project''' 

class Bag(object):

    def __init__(self):
        self.price = 0          # total price of the bag
        self.fruit = ''         # the only fruit
        self.vegetables = []    # the list of the 4 vegetables

    def __str__(self):
        return "i am a bag, yay. my price is: " % (self.price, self.num_items)


class OrganicThing(object):

    def __init__(self):
        self.name = ''              # name of the item
        self.category = ''          # fruit or vegetable
        self.price = 0              # price of the item
        self.pieces = 0             # number of pieces it is composed (ex. 1 for watermelon and 4 for apple)
        self.seasons = ['']         # season in which the item grows
        self.origin = ''            # regional, national, european or worldwide
        self.easyToPrepare = ''     # easy of difficult to prepare
        self.color = ''             # color of the item
        self.perishability = ''     # slow, normal or fast
        self.oftenUsed = ''         # whether the item is used to cook many things, such as onions and garlic
        self.forgotten = ''         # whether the item is forgotten or not
        self.recipes = []           # list of normal recipes names in which the item appears
        self.xmasRecipes = []       # list of Christmas recipes names in which the items appears

    def __str__(self):
        return "%s: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s." % (self.category, self.name, self.price, self.pieces, \
        self.seasons, self.origin, self.easyToPrepare, self.color, self.perishability, self.oftenUsed, self.forgotten)


class Recipe(object):

    def __init__(self):
        self.name = ''              # name of the recipe
        self.description = ''       # description
        self.ingredients = []       # list of ingredients
