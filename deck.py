import random


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
                cardValue = i + 1  # this way A = 1, 2 = 2, ..., J = 11, Q = 12, K = 13 etc
                # add the card to the deck dictionary
                self.deck[cardString] = cardValue

            # randomize the keys of the deck dictionary
            keys = list(self.deck.keys())
            random.shuffle(keys)

            # create randomized key-value pairs deck dictionary with randomized keys list
            self.deck = {key: self.deck[key] for key in keys}

    def dealCard(self):
        return self.deck.popitem()

    # use this method to deal a hand in the game of pig
    # hand will contain 4 cards
    # since the deck is in random order, it doesn't really matter if we deal the classic way,
    # or if we just give 4 cards in a row to each player :)
    def dealHand(self):
        hand = {}

        for i in range(4):
            cardString, cardValue = self.dealCard()
            hand[cardString] = cardValue

        return hand