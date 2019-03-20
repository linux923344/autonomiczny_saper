import pygame
from pygame.locals import *
from random import *
#from Bomb import Bomb

class BombRed:
    def __init__ (self):
        #dodaj .convert_alpha() w board
        self.sprite = pygame.image.load('sprites/bombR.png')
        self.code = 0

 