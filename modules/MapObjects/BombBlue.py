import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb


class BombBlue(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombB.png'
        super(BombBlue, self).__init__()
        self.defuseLevel = 2
