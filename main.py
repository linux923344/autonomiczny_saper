from modules.Board import Board
from modules.BombRed import BombRed
from modules.BombBlue import BombBlue
from modules.BombYellow import BombYellow
from modules.Saper import Saper
from modules.Stone import Stone
from modules.MapReader import *
from modules.PathFinder.PathFinder import PathFinder
from modules.Direction import Direction

board = Board(1480, 900)
reader = MapReader(board)
reader.read("maps/map_graph.txt")
s = Saper()
finder = PathFinder(board)
steps = finder.getPathTo(10, 7)
s.addSteps(steps)
board.addPlayer(s, 5, 0)
board.start()
