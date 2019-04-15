from modules.Board import Board
from modules.BombRed import BombRed
from modules.BombBlue import BombBlue
from modules.BombYellow import BombYellow
from modules.Saper import Saper
from modules.Converter import *
from modules.PathFinder.PathFinder import PathFinder

board = Board(1480, 900)
conv = Conventer(board)
conv.mapreader("maps/map_graph.txt")
# r = BombRed()
# board.addObject(r,5,1)
# b = BombBlue()
# board.addObject(b,6,1)
# y = BombYellow()
# board.addObject(y,7,7)
# s = Saper()
# board.addObject(s,0,0)
finder = PathFinder(board)
finder.getPathTo(0, 7)
board.start()
