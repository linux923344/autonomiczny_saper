import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb
from modules.MapObjects.Tool import Tool


class BombYellow(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombY.png'
        super(BombYellow, self).__init__()

    def defuse(self, tool):
        if(type(tool) is Tool):
            self.defuseLevel -= 1
            if (self.defuseLevel<=0):
                self.sprite = 'sprites/bombDefuse.png'
                self.timer = 0
        else:
            return False
