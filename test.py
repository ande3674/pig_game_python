import deck

def test():

    d = deck.Deck()

    for v in d.deck:
        print(v, d.deck[v])

    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    h = d.dealHand()

    for c in h:
        print(c, h[c])


    # f, x = d.dealCard()
    # g, y = d.dealCard()
    #
    # print(f)
    # print(x)
    #
    # print(g)
    # print(y)
    #
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    #
    for v in d.deck:
        print(v, d.deck[v])
    #
    # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

test()