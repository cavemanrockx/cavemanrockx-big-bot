from typing import List
from random import shuffle


class Card:

    """
    Cards for Uno with type and color

    Attributes
    -----------
    _color: color of the card
    _type: the number of the card or the type of card
    """

    _color: str
    _type: str
    _emoji: str

    def __init__(self, color, type, emoji):
        self._color = color
        self._type = type
        self._emoji = emoji

    def color_of(self):
        return self._color

    def type_of(self):
        return self._type

    def __str__(self):
        return f"[{self._color}:{self._type}]"

    def __repr__(self):
        return f"[{self._color}:{self._type}]"

    def __eq__(self, other):

        if (self._color == other.color_of()) and (self._type == other.type_of()):
            return True
        else:
            return False


class Deck:

    """
    Holds the cards in the deck

    Attributes
    ----------
    _deck: a deck containing all the cards
    _colors: colors of the cards
    _types: types of all the cards (includes numbers)
    """
    _deck: List[Card]
    _colors: List[str]
    _types: List[str]
    _emoji: List[str]

    def __init__(self):

        self._deck = []
        self._color = ["red", "blue", "green", "yellow", "black"]
        self._types = []

        for i in range(10):
            self._types.append(str(i))
        for i in range(5):
            abstract_types = ["skip", "reverse", "+2", "color_change", "+4"]
            self._types.append(abstract_types[i])

    def new_deck(self):

        self._deck = []

        for color in self._color:
            if color != "black":
                self._deck.append(Card(color, self._types[0]))
                for i in range(12):
                    self._deck.append(Card(color, self._types[i + 1]))
                    self._deck.append(Card(color, self._types[i + 1]))

            elif color == "black":
                for i in range(4):
                    self._deck.append(Card(color, self._types[13]))
                    self._deck.append(Card(color, self._types[14]))

    def shuffle(self):
        shuffle(self._deck)

    def remove(self):
        return self._deck.pop(0)

    def add(self, card: Card):
        self._deck.append(card)

    def last_card(self):
        return self._deck[len(self._deck)-1]

    def deck_list(self):
        return self._deck

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return str(self._deck)

    def __repr__(self):
        return str(self._deck)

    def __add__(self, other):

        list = other.deck_list()
        for i in list:
            self._deck.append(i)

        return self._deck


class Hand:

    """
    Holds the cards that belong to the players

    Attributes
    ----------
    _hand:  contains all the cards a player has
    """
    _hand: List[Card]

    def __init__(self):
        self._hand = []

    def add(self, card: Card) -> None:
        self._hand.append(card)

    def remove(self, card: Card):
        index = self._hand.index(card)
        self._hand.pop(index)

    def __len__(self):
        return len(self._hand)

    def show(self):
        return self._hand

    def __str__(self):
        return str(self._hand)

    def __repr__(self):
        return str(self._hand)


