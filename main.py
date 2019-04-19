from modules.Board.Board import Board
from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder

board = Board(1480, 900)
MapReader.read("maps/map1.txt", board)
s = Saper()
finder = PathFinder(board)
print(finder.getVertexByCords(3, 6))
steps = finder.getPathTo(3, 6)
s.addSteps(steps)
board.addPlayer(s, 5, 0)
board.start()
