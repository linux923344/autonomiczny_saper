import pygame
from pygame.locals import *
from modules.MapObjects.BombRed import *
from modules.MapObjects.BombBlue import *
from modules.MapObjects.BombYellow import *
from modules.Board.Board import *
from modules.MapObjects.Stone import *
from modules.MapObjects.Tool import Tool
from modules.MapObjects.Water import Water


class MapReader:
    def __init__(self, board):
        self.board = board

    def read(self, mapfile):
        f = open(mapfile, "r")
        mapa = f.read().split("\n")
        for indexline, line in enumerate(mapa):
            for indexrow, row in enumerate(line):
                #print(indexline, indexrow)
                if row == "R":
                    bomb = BombRed()
                    self.board.addObject(bomb, indexrow, indexline)
                elif row == "B":
                    bomb = BombBlue()
                    self.board.addObject(bomb, indexrow, indexline)
                elif row == "Y":
                    bomb = BombYellow()
                    self.board.addObject(bomb, indexrow, indexline)
                elif row == "S":
                    stone = Stone()
                    self.board.addObject(stone, indexrow, indexline)
                elif row == "T":
                    tool = Tool()
                    self.board.addObject(tool, indexrow, indexline)
                elif row == "W":
                    water = Water()
                    self.board.addObject(water, indexrow, indexline)

        f.close()
