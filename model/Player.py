from model.Piece import Piece
from model.Color import Color


class Player:
    def __init__(self, playerColor: Color):
        self.playerColor: playerColor = playerColor
        self.piece1: Piece = Piece(1, playerColor)
        self.piece2: Piece = Piece(2, playerColor)
        self.piece3: Piece = Piece(3, playerColor)
        self.piece4: Piece = Piece(4, playerColor)

    def getAllPieces(self) -> list[Piece]:
        return [self.piece1, self.piece2, self.piece3, self.piece4]
