import pygame
from pygame.locals import *
from random import *
from Bomb import Bomb

class BombYellow(Bomb):
    def __init__ (self):
        #dodaj .convert_alpha() w board
        self.sprite = pygame.image.load('../sprites/bombY.png')
        self.code = 0