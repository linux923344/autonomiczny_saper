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
    @staticmethod
    def read(mapfile, board):
        f = open(mapfile, "r")
        mapa = f.read().split("\n")
        for indexline, line in enumerate(mapa):
            for indexrow, row in enumerate(line):
                #print(indexline, indexrow)
                if row == "R":
                    bomb = BombRed()
                    bomb.setTimer(30)
                    board.addObject(bomb, indexrow, indexline)
                elif row == "B":
                    bomb = BombBlue()
                    bomb.setTimer(30)
                    board.addObject(bomb, indexrow, indexline)
                elif row == "Y":
                    bomb = BombYellow()
                    bomb.setTimer(30)
                    board.addObject(bomb, indexrow, indexline)
                elif row == "S":
                    stone = Stone()
                    board.addObject(stone, indexrow, indexline)
                elif row == "T":
                    tool = Tool()
                    board.addObject(tool, indexrow, indexline)
                elif row == "W":
                    water = Water()
                    board.addObject(water, indexrow, indexline)

        f.close()
