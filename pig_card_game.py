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
    discard = card_deck.dealCard()  # deal the next card for the discard pile

    while len(card_deck.deck) != 0:

        print("Number of cards left in pool: " + str(len(card_deck.deck)))
        print()

        if len(get_matches(hum.hand)) == 4 or len(get_matches(com.hand)) == 4:
            determine_winner(com.hand, hum.hand)
            break
        elif player == "human" and len(get_matches(hum.hand)) != 4:
            print("Human's hand: " + str(display_hand(hum.hand)))
            print("*No 4 of a kind for human.")

            print("Discard pile:")
            display_discard(discard)
            print()
            choice = input("Enter 'p' to pick up the discard pile, or 'd' to draw a new card: ")
            print()

            while choice != "d" and choice != "p": # !(choice == "d" or choice == "p")
                print("Error: invalid choice")
                choice = input("Enter 'p' to pick up the discard pile, 'd' to draw a new card: ")
                print()

            if choice == "d":
                hum.hand.update({card_deck.dealCard()})
                print("Human's hand: " + str(display_hand(hum.hand)))
                player, discard = hum.human_turn()
                print()

            elif choice == "p":
                #pick up discard pile
                hum.hand.update({discard})
                print("Human's hand: " + str(display_hand(hum.hand)))
                player, discard = hum.human_turn()
                print()


        elif player == "computer" and len(get_matches(com.hand)) != 4:
            print("*No 4 of a kind for computer.")
            print("*Computer plays.")
            # send discard value to want_discard() method and see if computer wants it...
            if com.want_discard(discard[1]):
                # pick up the discard card
                com.hand.update({discard})
                player, discard = com.computer_turn(get_matches(com.hand))
                print()

            # if not - then proceed normally, drawing a new card for the computer
            else:
                com.hand.update({card_deck.dealCard()})
                player, discard = com.computer_turn(get_matches(com.hand))
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

def display_discard(card):
    print(card[0])


main()