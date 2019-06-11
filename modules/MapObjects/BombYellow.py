import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb


class BombYellow(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombY.png'
        self.defuseLevel = 1
        super(BombYellow, self).__init__()
