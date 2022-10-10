from curses import ACS_GEQUAL


class Tree:

    def __init__(self,species,age,height,dbh,health,cut_down):

        # Define instance attributes
        self.species = species
        self.age = age
        self.height = height
        self.dbh = dbh
        self.health = health
        self.cut_down = cut_down

    def grow(self,years):
 
        if not years:
            print('Years parameter not provided!')
            return

        # Age the tree
        self.age += years

        # Add to tree height
        self.height += years * 3

        # Add to tree diameter
        self.dbh += years * 1

        return

    def squirrel_population(self):
        return int(self.dbh / 8)