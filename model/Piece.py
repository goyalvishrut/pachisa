from abc import ABC
from model.Color import Color
from model.Dice import Dice


class Piece(ABC):
    def __init__(self, pieceNumer: int, color: Color):
        self.symbol: str = color.name[0] + str(pieceNumer)
        self.color: Color = color
        self.currRow: int = self.color.homeRow
        self.currCol: int = self.color.homeCol

    def updateCurrRowCol(self, row: int, col: int):
        self.currRow = row
        self.currCol = col

    def getMovedRowCol(self, dice: Dice) -> tuple[int, int]:
        if (dice is Dice.TWENTY_FIVE and
                self.currRow == self.color.homeRow and self.currCol == self.color.homeCol):
            return 2, 2
        else:

            return self.currRow, self.currCol
