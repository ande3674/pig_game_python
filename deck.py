
class Deck:

    suits = ["hearts", "clubs", "diamonds", "spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.deck = {}
        # build the dictionary that represents the deck
        # we'll use the index i to create the value for each key-value pair
        for i in range(len(self.values)):
            # we need a card for each suit
            for suit in self.suits:
                # build the card string
                cardString = self.values[i] + ' of ' + suit
                # this way A = 1, 2 = 2, ..., J = 11, Q = 12, K = 13
                cardValue = i + 1
                # add the card to the deck dictionary
                self.deck[cardString] = cardValue

    def dealCard(self):
        return self.deck.popitem()