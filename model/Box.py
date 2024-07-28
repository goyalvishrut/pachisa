from model.Piece import Piece


class Box:
    def __init__(self, row: int, col: int):
        self.currentPieces: list[Piece] = []
        self.row = row
        self.col = col

    def __str__(self) -> str:
        result = ''
        if len(self.currentPieces) == 0:
            result = '--------'
        else:
            for i in self.currentPieces:
                result += i.symbol
        return result

    def addNewPiece(self, piece: Piece):
        self.currentPieces.append(piece)

    def removePiece(self, piece: Piece):
        self.currentPieces.remove(piece)


class Home(Box):
    def __init__(self, row: int, col: int, pieces: list[Piece]):
        super().__init__(row, col)
        self.currentPieces = pieces


class Destination(Box):
    def __init__(self, row: int, col: int):
        super().__init__(row, col)

    def __str__(self) -> str:
        return '--HOME--'
