from constants import *
from card import *


class Play:
    def __init__(self, cards: list[Card]):
        if not cards:
            raise InvalidPlayError("Play cannot be empty")
        self._cards = cards
        length = len(cards)
        values = sorted(c.get_int_value() for c in cards)
        suits = [c.get_int_suit() for c in cards]
        unique_values = set(values)
        value = 0

        if len(unique_values) == 1 and length <= 4:
            value += MATCH_INCR * length

        elif length == 4 and len(unique_values) == 2 and sorted([values.count(v) for v in unique_values]) == [2,2]:
            value += 50000

        elif length >= 3 and all(values[i] + 1 == values[i+1] for i in range(length-1)):
            same_suit = len(set(suits)) == 1
            S_bit = 1 if same_suit else 0
            value += 60000 + (length-3)*10000 + S_bit*1000
        else:
            raise InvalidPlayError("Invalid play")


        highest_card = max(cards, key=lambda c: c.get_int_value())
        value += highest_card.get_int_value() * 10
        value += max(cards, key=lambda c: c.get_int_suit()).get_int_suit()

        self._value = value

    def get_value(self) -> int:
        return self._value

    def get_cards(self) -> list[Card]:
        return self._cards

    def compare(self, play: "Play") -> int:
        if type(play) == EmptyPlay:
            return 1
        if self._value // 10000 != play.get_value() // 10000:
            raise InvalidPlayError("Play is not the same type as previous play")
        return self._value - play.get_value()

    def to_string(self) -> str:
        string = ""
        for c in self._cards:
            string += c.to_string() + " "
        return string.strip()


class EmptyPlay(Play):
    def __init__(self):
        self._value = -1
        self._cards = []


'''
value of a play is an integer (T)TSCCU:
(T)T: (0)1 - 12
    - type of play, extra digit is needed for longer straights
S: 0 - 1
    - only applies to straights, 1 if they are the same suit
CC: 0 - 12
    - highest card value, index from VALUES
U: 0 - 3
    - highest suit value, index from SUITS
'''
