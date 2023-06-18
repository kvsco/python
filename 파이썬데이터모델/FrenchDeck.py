import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

####
if __name__ == "__main__":
    f_card = Card('7', 'diamonds')
    print(f_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[1])
    print(deck[2])
    print(deck[-1])

    # iteration
    for card in deck:
        print(card)
    print("-"*30)
    for card in reversed(deck):
        print(card)