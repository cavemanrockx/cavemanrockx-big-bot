from cogs.uno.deck import Card, Hand, Deck
from typing import Dict, List


class unoGame:

    _players: List[str]
    _player_hands: Dict[str, Hand]
    temp_bool: bool
    play_deck: Deck
    drop_deck: Deck
    play_color: str
    current_player: int
    player_constant: int


    def __init__(self, players: List[str]):
        self._players = players
        self._player_hands = {}
        self.play_color = ""
        self.current_player = 0
        self.player_constant = 1


        self.play_deck = Deck()
        self.play_deck.new_deck()
        self.play_deck.shuffle()

        self.drop_deck = Deck()

        for player in self._players:
            self._player_hands[player] = Hand()

    def start(self):

        for player in self._players:
            for i in range(7):
                self._player_hands[player].add(self.play_deck.remove())

        starting_card = self.play_deck.remove()
        self.drop_deck.add(starting_card)
        self.play_color = starting_card.color_of()

    def pickup(self, player: str):
        self._player_hands[player].add((self.play_deck.remove()))

    def try_drop(self, player: str, card: Card):

        if self.is_valid_drop(card):
            self._player_hands[player].remove(card)
            self.play_color = card.color_of()
            self.drop_deck.add(card)

            #do action now, since all action affect next player
            self.actions(card)


    def next_player(self):
        if self.player_constant == 1:
            self.current_player += self.player_constant
            self.current_player = self.current_player % len(self._players)
            return self.current_player
        elif self.player_constant == -1:
            self.current_player += self.player_constant
            if self.current_player < 0:
                self.current_player = (len(self._players) - 1)
            return self.current_player

    def show_hand(self, player: str):
        return self._player_hands[player]

    def is_valid_drop(self, card):
            if card.type_of() == self.drop_deck.last_card().type_of():

                return True
            elif card.color_of == "black":

                return True

            elif card.color_of() == self.play_color:
                return True
            else:
                return False

    def actions(self, card):

        types = ["skip", "reverse", "+2", "color_change", "+4"]
        if card.type_of() == "skip":
            self.next_player()
            self.next_player()
        elif card.type_of() == "reverse":
            if self.player_constant == -1:
                self.player_constant = 1
            else:
                self.player_constant = -1
            self.next_player()
        elif card.type_of() == "+2":
            player = self._players[self.next_player()]
            self._player_hands[player].add(self.play_deck.remove())
            self._player_hands[player].add(self.play_deck.remove())
        elif card.type_of() == "+4":
            player = self._players[self.next_player()]
            self._player_hands[player].add(self.play_deck.remove())
            self._player_hands[player].add(self.play_deck.remove())
            self._player_hands[player].add(self.play_deck.remove())
            self._player_hands[player].add(self.play_deck.remove())

    def play_deck_is_empty(self):
        if len(self.play_deck) <= 0:
            return True
        return False

    def turn_drop_deck(self):
        self.play_deck.__add__(self.drop_deck)
        self.play_deck.shuffle()










"""
if __name__ == "__main__":

    a = unoGame(["bob","rob"])
    print(a)
    a.start()
"""