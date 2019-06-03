#!/usr/bin/python
from modules.Board.Board import Board
from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder

board = Board(1480, 900)
mapName = "map15"
MapReader.read("maps/"+mapName + ".txt", board)
s = Saper()
#steps = PathFinder.getPathToByDfs(board, 3, 6)
#steps = PathFinder.getPathToByBFS(board, 3, 6)
steps = PathFinder.getPathToByBestFirstSearch(board, mapName)
s.addSteps(steps)
# board.setMachineLearningWalkning()
board.addPlayer(s, 5, 0)
board.start()
