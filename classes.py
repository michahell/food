'''
Filip Ilievski
Emanuele Crosato
Michael Trouw
'''

class Bag(object):

    def __init__(self):
        self.price = 0
        self.num_items = 0

    def getPrice(self):
        return self.price

    def getNumItems(self):
        return self.num_items

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

    def __str__(self):
        return "organic thing, %s, %s, %s, %s" % (self.name, self.category, self.price, self.piece_size)





