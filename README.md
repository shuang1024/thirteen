# Thirteen
2-4 player card-shedding game.

- **Note:** Cards will be represented as [value][suit] (i.e. 4S for four of spades or KH for king of hearts), as well as individual card values and suits (i.e. K or H).

## Setup
Each player is delt 13 cards from a standard 52 card deck with no repeats, ranging from the lowest value of 3 up to the highest value of 2 (3, 4, 5, 6, 7, 8, 9, 10, J(ack), Q(ueen), K(ing), A(ce), 2). Suits in increasing value are S(pades), D(iamonds), C(lubs), H(earts).

## Gameplay
The player with the 3 of spades (lowest card value) will start.

Each player must place a card or combination of cards, also called a play, that has a greater value but are the same type than the previous play.

Compare card value using the smallest value of a play (comparing with a different index won't make a difference, just make sure to use the same index for both plays).

- Suits also matter, but **only if two plays have the same card values**. To compare two plays with the same card values, the play that has the card with the higher value and suit will be stronger. However, card value will always have higher priority.

The first player has the choice to play any valid type they want. If a play is made by a player and nobody can push any higher, all previous plays are discarded and said player can place any play of any value.

Types of plays are:
- Single
    - 4S < 7C (4 < 7)
    - KS < KH (looking at K's, S < H)
- Pair
    - 3S 3C < 4S 4C (3 < 4)
    - 3S 3C < 3D 3H (looking at 3's, C < H)
- Triple
    - 4D 4C 4H < 7S 7D 7H (4 < 7)
    - Suits do not need to be checked since there are only 4 cards of each type
- Quadruple or quad
    - 4S 4D 4C 4H < 7S 7D 7C 7H (4 < 7)
    - Again, suits do not need to be checked since there are only 4 cards of each type
- Two consecutive pairs or two-pair
    - 5S 5D 6D 6C < JD JH QS QD (5 < J)
    - 8S 8D 9S 9C < 8C 8H 9D 9H (looking at 9's, C < H)
- Sequence or straight of 3+
    - Cards with consecutive values up to and including ace (i.e. KC AH **2D** is invalid).
    - Different lengths are distinct types (i.e. cannot play sequence of 4 after sequence of 3)
    - Same suit > different suit, but they are still considered the same type if they have the same length
    - 3H 4C 5H < 5S 6C 7D (3 < 5)
    - 9D 10C JD QD < 9H 10D JC QS (looking at Q's, C < H)
    - 8S 9C 10H < 8D 9D 10D (different < same suit)
