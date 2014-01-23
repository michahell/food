'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

class Bag(object):

    def __init__(self):
        self.price = 0
        self.fruit = ''
        self.vegetables = []

    def __str__(self):
        return "i am a bag, yay. my price is: " % (self.price, self.num_items)


class OrganicThing(object):

    def __init__(self):
        self.name = ''
        self.category = ''
        self.price = 0
        self.pieces = 0
        self.seasons = ['']
        self.origin = ''
        self.easyToPrepare = ''
        self.color = ''
        self.perishability = ''
        self.oftenUsed = ''
        self.forgotten = ''
        self.recipes = []
        self.xmasRecipes = []

    def __str__(self):
        return "%s: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s." % (self.category, self.name, self.price, self.pieces, \
        self.seasons, self.origin, self.easyToPrepare, self.color, self.perishability, self.oftenUsed, self.forgotten)


class Recipe(object):

    def __init__(self):
        self.name = ''
	self.description = ''
        self.ingredients = []
