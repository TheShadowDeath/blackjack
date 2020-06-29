from itertools import product
from random import shuffle
from consts import SUITS, RANKS


class Card:

    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self):
        message = self.rank + ' ' + self.suit + '\nPoints: ' + str(self.points) + '\n'
        return message


class Deck:

    def __init__(self):
        self.cards = self._create_deck()
        shuffle(self.cards)

    def _create_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10

            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)

        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
