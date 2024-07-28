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
        one = [Dice.ONE] * 5
        two = [Dice.TWO] * 10
        three = [Dice.THREE] * 10
        five = [Dice.FIVE] * 1
        eight = [Dice.EIGHT] * 5
        twentyfive = [Dice.TWENTY_FIVE] * 1
        dice = one + two + three + five + eight + twentyfive
        return random.choice(dice)
