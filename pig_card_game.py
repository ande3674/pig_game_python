import collections
import deck
import human
import computer


def main():
    com = computer.Computer()
    hum = human.Human()
    card_deck = deck.Deck()

    com.hand = card_deck.dealHand()
    hum.hand = card_deck.dealHand()

    player = "human"

    while len(card_deck.deck) != 0:

        print("Number of cards left in pool: " + str(len(card_deck.deck)))
        print()

        if len(get_matches(hum.hand)) == 4 or len(get_matches(com.hand)) == 4:
            determine_winner(com.hand, hum.hand)
            break
        elif player == "human" and len(get_matches(hum.hand)) != 4:
            print("Human's hand: " + str(display_hand(hum.hand)))
            print("*No 4 of a kind for human.")
            print("*Draws a card from the top of the deck.")
            hum.hand.update({card_deck.dealCard()})
            print("Human's hand: " + str(display_hand(hum.hand)))
            player = hum.human_turn()
            print()
        elif player == "computer" and len(get_matches(com.hand)) != 4:
            print("*No 4 of a kind for computer.")
            print("*Draws a card from the top of the deck.")
            com.hand.update({card_deck.dealCard()})
            player = com.computer_turn(get_matches(com.hand))
            print()

    if len(card_deck.deck) == 0:
        print()
        print("Pool is empty. Who has the most matches? ")
        determine_winner(com.hand, hum.hand)


def determine_winner(com_hand, hum_hand):

    print("Computer's hand: " + str(display_hand(com_hand)))
    print("Human's hand: " + str(display_hand(hum_hand)))

    comp_matches = len(get_matches(com_hand))
    hum_matches = len(get_matches(hum_hand))

    if comp_matches == hum_matches:
        print("It's a tie!")
    elif comp_matches > hum_matches:
        print("Computer wins!")
    else:
        print("Human wins!")


def display_hand(hand):

    return [card for card in hand.keys()]


def get_matches(hand):

    matches = []

    # get a counter list of all the values and their count
    counter = collections.Counter(hand.values())

    max_count_value = list(counter.values())[0]
    max_value = list(counter.keys())[0]

    # get the higher value card with the most matches
    for key, value in counter.items():
        # if the number of matches are equal
        # assign the higher value to max value
        if value == max_count_value:
            if max_value < key:
                max_value = key
                max_count_value = value
        elif value > max_count_value:
            max_count_value = value
            max_value = key

    # make a list of the higher value card with the most matches
    if max_count_value > 1:
        for x in range(max_count_value):
            matches.append(max_value)

    return matches


main()
