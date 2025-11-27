VALUES = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

SUITS = ["S", "D", "C", "H"]

MATCH_INCR = 10000 # 1 card multiplies by 1 => 10000, 2 cards by 2 => 20000, etc.
TWO_PAIR = 50000
STR_BASE = 60000
STR_INCR = 10000 # length of 3 adds 0 => 60000, 4 adds 10000 => 70000, etc.

class InvalidPlayError(Exception): pass

class InvalidGameError(Exception): pass
