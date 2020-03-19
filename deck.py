from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        for i in range(0, 4):
            for j in range(2, 15):
                self.deck.append(Card(j, i))
        pass

    def size(self):
        return len(self.deck)

    def draw_card(self):
        if(len(self.deck) == 0):
            return None
        index = random.randint(0, len(self.deck)-1)
        card = self.deck[index].copy()
        del self.deck[index]
        return card

    def guessColor(self):
        redCount = 0
        blackCount = 0
        for card in self.deck:
            if card.color == 'red':
                redCount += 1
            else:
                blackCount += 1
        print('red:', redCount, 'black:', blackCount)
        if redCount > blackCount:
            return 'red'
        else:
            return 'black'
        return round(redCount/(redCount + blackCount))

    def guessHighLow(self, initial):
        highCount = 0
        lowCount = 0
        for card in self.deck:
            if card.value > initial:
                highCount += 1
            if card.value < initial:
                lowCount += 1
        print('initial', initial, 'high:', highCount, 'low:', lowCount)
        if highCount > lowCount:
            return 1
        else:
            return 0

    def guessInOut(self, val1, val2):
        inside = 0
        outside = 0
        for card in self.deck:
            if card.value < val1 and card.value > val2 or card.value > val1 and card.value < val2:
                inside += 1
            elif card.value != val1 and card.value != val2:
                outside += 1
        # if 1 -> guess is outside
        if outside > inside:
            print('guessing outside of ', val1, val2)
            return 1
        else:
            print('guessing inside of ', val1, val2)
            return 0

    def guessType(self):
        arr = [0, 0, 0, 0]
        for card in self.deck:
            arr[card.type] += 1
        # Returns the type for the most common element in array
        print(arr)
        return arr.index(max(arr))

    def printDeck(self):
        for card in self.deck:
            card.print_card()


L
