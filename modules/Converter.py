import pygame
from pygame.locals import * 
from modules.BombRed import * 
from modules.Board import * 
class Conventer:
    def __init__(self, board):
        self.board = board

    def mapreader(self, mapfile):
        f = open(mapfile,"r")
        mapa = f.read().split("\n")
        for indexline, line in enumerate(mapa) : 
            for indexrow, row in enumerate(line) :
                print(indexline, indexrow)
                if row == "S" :
                    bomb=BombRed()
                    self.board.addObject(bomb, indexrow, indexline)
        f.close() 
