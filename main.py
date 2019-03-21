from modules.Board import Board
from modules.BombRed import BombRed

board = Board(1480, 900)
red = BombRed()
board.addObject(red,5,1)
board.start()