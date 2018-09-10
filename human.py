
class Human:

    def __init__(self):
        self.hand = {}

    def human_turn(self):

        discard_card = input("Which card do you want to remove from your hand? ")

        # if card in hand return the card value, otherwise return 0
        card = self.hand.pop(discard_card, 0)

        while card == 0:
            print("You don't have that card.")
            discard_card = input("Which card do you want to remove from your hand? ")
            card = self.hand.pop(discard_card, 0)

        return "computer"
