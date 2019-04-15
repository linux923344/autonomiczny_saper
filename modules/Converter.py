import pygame
from pygame.locals import *
from modules.BombRed import *
from modules.BombBlue import *
from modules.BombYellow import *
from modules.Board import *
from modules.Stone import *


class Conventer:
    def __init__(self, board):
        self.board = board

    def mapreader(self, mapfile):
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
        f.close()
