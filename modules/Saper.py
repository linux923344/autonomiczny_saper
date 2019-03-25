import pygame
from pygame.locals import *
from random import *

class Saper:
    def __init__ (self):
        self.walkRight='sprites/r.png'
        self.walkLeft = 'sprites/l.png'
        self.walkUp= 'sprites/u.png'
        self.walkDown= 'sprites/d.png'
        self.sprite = self.walkDown

