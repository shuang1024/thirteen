from constants import *


class Card:
    def __init__(self, value: str, suit: str):
        self.__value = value
        self.__suit = suit

    def __eq__(self, other):
        return isinstance(other, Card) and self.get_value() == other.get_value() and self.get_suit() == other.get_suit()

    def __hash__(self):
        return hash((self.get_value(), self.get_suit()))

    def get_value(self) -> str:
        return self.__value

    def get_int_value(self) -> str:
        return VALUES.index(self.__value)

    def get_suit(self) -> str:
        return self.__suit

    def get_int_suit(self) -> str:
        return SUITS.index(self.__suit)

    def compare(self, card: Card) -> int:
        if type(self) != type(card):
            raise InvalidPlayError("Cannot compare different play types")
        if card.get_value() != self.__value:
            return self.get_int_value() - card.get_int_value()
        return self.get_int_suit() - card.get_int_suit()

    def to_string(self) -> str:
        return self.__value + self.__suit
