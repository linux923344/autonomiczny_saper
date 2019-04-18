from modules.Board.Board import Board
from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder

board = Board(1480, 900)
reader = MapReader(board)
reader.read("maps/map_graph.txt")
s = Saper()
finder = PathFinder(board)
steps = finder.getPathTo(10, 7)
s.addSteps(steps)
board.addPlayer(s, 5, 0)
board.start()
