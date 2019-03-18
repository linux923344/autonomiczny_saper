from typing import List, Any

import pygame
from pygame.locals import *
from random import *

class Board:
    def __init__(self, x, y):
        self.x=x    
        self.y=y

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption("Saper")
        self.background=pygame.image.load('sprites/pole.png')
        self.window.blit(self.background,(0,0))
        pygame.display.update()
        self.run = True

        while (self.run):
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

    

    def close(self):
        self.run = False
        pygame.quit()


        