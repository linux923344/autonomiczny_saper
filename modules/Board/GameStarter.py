import sys
from modules.Board.Board import Board
from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder
from modules.menuWindow.AlgorythmType import AlgorythmType


class GameStarter:

    @staticmethod
    def run(mapPaht, algorytmType):
        board = Board(1480, 900)
        mapName = mapPaht.replace(".txt", "")
        MapReader.read("./maps/"+mapPaht, board)
        s = Saper()

        if(algorytmType == "AlgorythmType.BEST_FIRST_SEARCH"):
            steps = PathFinder.getPathToByBestFirstSearch(board, mapName)
            s.addSteps(steps)
        elif(algorytmType == "AlgorythmType.BREADTH_FIRST_SEARCH"):
            steps = PathFinder.getPathToByBFS(board, 3, 6)
            s.addSteps(steps)
        elif(algorytmType == "AlgorythmType.DFS"):
            steps = PathFinder.getPathToByDfs(board, 3, 6)
            s.addSteps(steps)
        elif(algorytmType == "AlgorythmType.VOWPAL_WABBIT"):
            board.setMachineLearningWalkning(WalkingType.VOWLPAL_WALKER)
        elif(algorytmType == "AlgorythmType.DECISION_TREE"):
            board.setMachineLearningWalkning(WalkingType.DECISION_TREE_WALKER)

        board.addPlayer(s, 5, 0)
        board.start()
