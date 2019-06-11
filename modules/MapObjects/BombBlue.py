import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb
from modules.MapObjects.Tool import Tool


class BombBlue(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombB.png'
        super(BombBlue, self).__init__()
        self.defuseLevel = 2

    def defuse(self, tool):
        if(type(tool) is Tool):
            self.defuseLevel -= 1
        else:
            return False
