from constants import *
from card import *
from play import *


class Hand:
    def __init__(self, hand: list[Card]):
        self.__hand = hand

    def play(self, str_cards: str) -> Play:
        str_cards = str_cards.split(" ")
        cards = []
        for str_card in str_cards:
            card = Card(str_card[:-1], str_card[-1])
            if card not in self.__hand:
                raise InvalidPlayError(f"{str_card} not in hand")
            cards.append(card)

        for c in cards:
            self.__hand.remove(c)

        play = Play(cards)
        return play

    def has_cards(self) -> bool:
        return len(self.__hand) > 0

    def to_string(self) -> str:
        string = ""
        for c in self.__hand:
            string += c.to_string() + " "

        return string.strip()
