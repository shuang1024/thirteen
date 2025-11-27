import random

from constants import *
from card import *
from play import *
from hand import *


class Game:
    def __init__(self, num_players: int):
        if num_players < 2 or num_players > 4:
            raise InvalidGameError("Number of players must be between 2 and 4 inclusive")

        self.__num_players = num_players
        self.__deck = []
        self.__shuffle()
        self.__hands = []
        for i in range(self.__num_players):
            self.__hands.append(Hand(sorted(self.__deck[i * 13:(i+1) * 13], key=lambda c: c.get_int_value()*10 + c.get_int_suit())))
        self.__player = 0

        self.__prev_play = EmptyPlay()
        self.__curr_play = EmptyPlay()

        self.__rank = []
        self.__skip_count = 0

    def get_curr_player(self) -> int:
        return self.__player

    def get_curr_hand(self) -> Hand:
        return self.__hands[self.__player]

    def get_prev_play(self) -> Play:
        return self.__prev_play

    def __shuffle(self) -> None:
        for v in VALUES:
            for s in SUITS:
                self.__deck.append(Card(v, s))
        random.shuffle(self.__deck)

    def play(self, str_play: str) -> Play:
        if str_play == "skip":
            self.__skip_count += 1
            if self.__skip_count >= self.__num_players - 1:
                self.__prev_play = EmptyPlay()
                self.__skip_count = 0
            return EmptyPlay()
        else:
            try:
                self.__curr_play = self.__hands[self.__player].play(str_play)
                if not self.__hands[self.__player].has_cards():
                    self.__rank.append(self.__player)
                    self.__hands.pop(self.__player)
                    self.__num_players -= 1
                if self.__curr_play.compare(self.__prev_play) <= 0:
                    raise InvalidPlayError("Current play must be greater than previous play")
                else:
                    self.__prev_play = self.__curr_play
                    self.__skip_count = 0
                    return self.__curr_play
            except InvalidPlayError as e:
                raise

    def next_player(self) -> None:
        self.__player += 1
        self.__player %= self.__num_players
