from enum import Enum


class Color(Enum):
    # def __init__(self, player_name1, player_name2):
    #     self.white_piece_player_name = player_name1
    #     self.black_piece_player_name = player_name2

    RED = (0, 4, 2, 4, 1, 3, 2)
    GREEN = (1, 2, 4, 3, 4, 2, 3)
    BLUE = (2, 0, 2, 0, 3, 1, 2)
    YELLOW = (3, 2, 0, 1, 0, 2, 1)

    def __new__(cls, value, row, col, innerEntryRow, innerEntryCol, destinationEntryRow, destinationEntryCol):
        __obj = object.__new__(cls)
        __obj._value_ = value
        __obj.homeRow = row
        __obj.homeCol = col
        __obj.innerEntryRow = innerEntryCol
        __obj.innerEntryCol = innerEntryCol
        __obj.destinationEntryRow = destinationEntryRow
        __obj.destinationEntryCol = destinationEntryCol
        return __obj
