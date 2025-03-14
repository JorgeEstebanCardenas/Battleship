from enum import Enum

class States(Enum):
    EMPTY = 1
    MISS = 2
    HIT = 3
    SHIP = 4

class Results(Enum):
    MISS=0
    HIT=1
    SUNK_2=2
    SUNK_3=3
    SUNK_4=4
    SUNK_5=5
