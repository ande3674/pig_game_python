
class Computer:

    def __init__(self):
        self.hand = {}

    def computer_turn(self, matches):

        no_match_cards = []
        number_of_matches = len(matches)

        if number_of_matches != 0:
            for key, value in self.hand.items():
                # if value doesn't match the first
                # value in match, add value to no match list
                if value != matches[0]:
                    no_match_cards.append(key)
            # remove from hand the first value with no matches
            return "human", (no_match_cards[0], self.hand.pop(no_match_cards[0]))
        else:
            return "human", self.hand.popitem()


    def want_discard(self, discard_val):
        want = False

        for val in self.hand.values():
            if val == discard_val:
                want = True

        return want