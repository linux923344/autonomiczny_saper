import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb


class BombRed(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombR.png'
        super(BombRed, self).__init__()
