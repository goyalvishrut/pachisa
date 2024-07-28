import random

from model.Board import Board
from model.Dice import Dice
from model.Color import Color

if __name__ == '__main__':
    board = Board()
    board.printCurrentBoard()
    while True:
        a = input("input")
        if a == 'q':
            exit(100)
        # elif a == 'r':
        #     move = Dice.rollDice()
        #     print(move)
        #     piece = input("input")
        #     board.movePiece(piece, move)
        else:
            print(Dice.rollDice())
