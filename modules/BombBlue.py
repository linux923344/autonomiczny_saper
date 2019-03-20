import pygame
from pygame.locals import *
from random import *
from Bomb import Bomb

class BombBlue(Bomb):
    def __init__ (self):
        self.sprite = pygame.image.load('../sprites/bombB.png')
        self.code = 0

    