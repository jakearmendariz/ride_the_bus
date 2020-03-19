
class Card:
    value = 0
    name = ''
    type = 0
    color = ''
    # Type: 0 == heart, 1 == diamond, 2 == spades, 3 == clubs

    def __init__(self, value, type):
        self.value = value
        if self.value == 11:
            self.name = 'Jack'
        elif self.value == 12:
            self.name = 'Queen'
        elif self.value == 13:
            self.name = 'King'
        elif self.value == 14:
            self.name = 'Ace'
        else:
            self.name = str(self.value)

        if type < 2:
            self.color = 'red'
        else:
            self.color = 'black'

        self.type = type

    # Returns an identical copy of card
    def copy(self):
        return Card(self.value, self.type)

    def print_card(self):
        if self.type == 0:
            print(self.name, 'of hearts')
        elif self.type == 1:
            print(self.name, 'of diamonds')
        elif self.type == 2:
            print(self.name, 'of spades')
        elif self.type == 3:
            print(self.name, 'of clubs')
        else:
            print(self.name, 'of', self.type)

    def toString(self):
        if self.type == 0:
            return str(self.name + ' of hearts')
        elif self.type == 1:
            return str(self.name + ' of diamonds')
        elif self.type == 2:
            return str(self.name + ' of spades')
        elif self.type == 3:
            return str(self.name + ' of clubs')
        else:
            return str(self.name + ' of ' + self.type)

    @staticmethod
    def typeToString(type):
        if type == 0:
            return 'hearts'
        elif type == 1:
            return 'diamonds'
        elif type == 2:
            return 'spades'
        elif type == 3:
            return 'clubs'
        else:
            return 'NA'
