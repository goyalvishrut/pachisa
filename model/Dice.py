import random
from enum import Enum


class Dice(Enum):
    ONE = 1  # (5 / 32)
    TWO = 2  # (10 / 32)
    THREE = 3  # (10 / 32)
    FIVE = 5  # (1 / 32)
    EIGHT = 8  # (5 / 32)
    TWENTY_FIVE = 25  # (1 / 32)

    @staticmethod
    def rollDice() -> 'Dice':
        return random.choice(list(Dice))
