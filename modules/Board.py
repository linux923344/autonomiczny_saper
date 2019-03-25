from typing import List, Any

import pygame
from pygame.locals import *
from random import *

DISPLACEMENT_Y = 63
DISPLACEMENT_X = 45
SQUARE_SIZE = 100

class Board:
    def __init__(self, x, y):
        self.x=x    
        self.y=y
        self.board = [[None for j in range(12)]for i in range(8)]
        
        

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption("Saper")
        self.background=pygame.image.load('sprites/pole.png')
        
        
        self.run = True

        while (self.run):
            pygame.time.delay(100)
            
            
            self.renderSprites()
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

    def addObject(self,game_object,x,y):
        self.board[y][x] = game_object

    def renderSprites(self):
        self.window.blit(self.background,(0,0))
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x!=None):
                    sprite=pygame.image.load(x.sprite).convert_alpha()
                    self.window.blit(sprite,(DISPLACEMENT_X + index_x*SQUARE_SIZE,
                    DISPLACEMENT_Y + index_y*SQUARE_SIZE))

    def close(self):
        self.run = False
        pygame.quit()
Euterpea