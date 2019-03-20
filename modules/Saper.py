import pygame
from pygame.locals import *
from random import *

class Saper:
    def __init__ (self):
        self.walkRight=pygame.image.load('../sprites/r.png')
        self.walkLeft = pygame.image.load('../sprites/l.png')
        self.walkUp=pygame.image.load('../sprites/u.png')
        self.walkDown=pygame.image.load('../sprites/d.png')

