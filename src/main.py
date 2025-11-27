import os

from constants import *
from card import *
from play import *
from hand import *
from game import *

clear = lambda: os.system("cls")

num_players = int(input("Number of players: "))
while True:
    try:
        game = Game(num_players)
    except InvalidGameError as e:
        print(f"InvalidGameError: {e}")
        num_players = int(input("Number of players: "))
    else:
        break


while True:
    clear()
    print(f"Player {game.get_curr_player()}'s turn")
    print(game.get_curr_hand().to_string())
    print(f"Previous play: {game.get_prev_play().to_string() if game.get_prev_play().get_cards() else 'None'}")

    play = input("Play: ")
    while True:
        try:
            game.play(play)
        except InvalidPlayError as e:
            print(f"InvalidPlayError: {e}")
            play = input("Play: ")
        else:
            break

    game.next_player()
