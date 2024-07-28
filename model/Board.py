from model.Player import Player
from model.Box import Box, Home, Destination
from model.Color import Color
from model.Piece import Piece
from model.Dice import Dice


class Board:

    def __init__(self):
        player1Color = Color.RED
        player2Color = Color.GREEN
        player3Color = Color.BLUE
        player4Color = Color.YELLOW
        self.__player1 = Player(player1Color)
        self.__player2 = Player(player2Color)
        self.__player3 = Player(player3Color)
        self.__player4 = Player(player4Color)
        self.__currentBoard: list[list[Box | Home]] = self.__generateBoard()
        self.currentPlayerChance: Color = player1Color

    def __generateBoard(self):
        board: list[list[Box | Home]] = []
        for r in range(5):
            board.append([])
            for c in range(5):
                board[r].append(self.__getBoxForPos(r, c))
        return board

    def __getBoxForPos(self, r: int, c: int) -> Box:
        if r == c == 2:
            return Destination(r, c)
        elif r == 4 and c == 2:
            return Home(r, c, self.__player1.getAllPieces())
        elif r == 2 and c == 4:
            return Home(r, c, self.__player2.getAllPieces())
        elif r == 0 and c == 2:
            return Home(r, c, self.__player3.getAllPieces())
        elif r == 2 and c == 0:
            return Home(r, c, self.__player4.getAllPieces())
        else:
            return Box(r, c)

    def __getHomeForPlayer(self, color: Color) -> Home:
        return self.__currentBoard[color.homeRow][color.homeCol]

    def printCurrentBoard(self):
        iterations = len(self.__currentBoard)
        print(iterations)
        for r in range(iterations):
            for c in range(iterations):
                box = self.__currentBoard[r][c]
                print(str(box), end=" ")
            print('\n', end="")
        print()

    def print1(self):
        print(self.__currentBoard)

    def movePiece(self, piece: Piece, dice: Dice):
        newRow, newCol = self.__getNewRowCol(piece, dice)
        self.__currentBoard[piece.currRow][piece.currCol].removePiece(piece)
        self.__currentBoard[newRow][newCol].addNewPiece(piece)
        piece.updateCurrRowCol(newRow, newCol)

    def __getNewRowCol(self, piece: Piece, dice: Dice) -> tuple[int, int]:
        pass
