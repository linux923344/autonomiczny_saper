import pygame
from pygame.locals import *
from random import *

import queue


class Saper:
    def __init__(self):
        self.walkRight = 'sprites/r.png'
        self.walkLeft = 'sprites/l.png'
        self.walkUp = 'sprites/u.png'
        self.walkDown = 'sprites/d.png'
        self.sprite = self.walkDown
        self.steps = queue.Queue()
        self.equipment = []

    def addSteps(self, stepsList):
        for step in stepsList:
            self.steps.put(step)

    def pickUp(self, item):
        print(item)
        self.equipment.append(item)
