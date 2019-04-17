from typing import List, Any

import pygame
from pygame.locals import *
from random import *
from modules.Direction import Direction
from modules.Tool import Tool

DISPLACEMENT_Y = 45
DISPLACEMENT_X = 33
SQUARE_SIZE = 100


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[None for j in range(12)]for i in range(8)]

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Saper")
        self.background = pygame.image.load('sprites/pole.png')
        self.run = True

        while (self.run):
            pygame.time.delay(100)

            self.renderSprites()
            pygame.display.update()

            if(not self.player.steps.empty()):
                direction = self.player.steps.get()
                self.walk(direction)

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

            # Tymczasowe manulane chodzenie
                if event.type == KEYDOWN:

                    if (event.key == K_LEFT):
                        self.walk(Direction.LEFT)
                    if (event.key == K_RIGHT):
                        self.walk(Direction.RIGHT)
                    if (event.key == K_DOWN):
                        self.walk(Direction.DOWN)
                    if (event.key == K_UP):
                        self.walk(Direction.UP)

    def walk(self, direction):
        cords = self.getCordsOf(self.player)
        cord_x = cords[0]
        cord_y = cords[1]
        del cords
        if(direction == Direction.LEFT):
            self.board[cord_y][cord_x].sprite = self.board[cord_y][cord_x].walkLeft
            if(cord_x > 0 and self.board[cord_y][cord_x - 1] == None):
                self.board[cord_y][cord_x - 1] = self.board[cord_y][cord_x]
            elif(cord_x > 0 and type(self.board[cord_y][cord_x - 1]) is Tool):
                self.player.pickUp(self.board[cord_y][cord_x - 1])
                self.board[cord_y][cord_x - 1] = self.board[cord_y][cord_x]
            else:
                return False
        elif(direction == Direction.RIGHT):
            self.board[cord_y][cord_x].sprite = self.board[cord_y][cord_x].walkRight
            if(cord_x < 11 and self.board[cord_y][cord_x + 1] == None):
                self.board[cord_y][cord_x + 1] = self.board[cord_y][cord_x]
            elif(cord_x > 0 and type(self.board[cord_y][cord_x + 1]) is Tool):
                self.player.pickUp(self.board[cord_y][cord_x + 1])
                self.board[cord_y][cord_x + 1] = self.board[cord_y][cord_x]
            else:
                return False
        elif(direction == Direction.DOWN):
            self.board[cord_y][cord_x].sprite = self.board[cord_y][cord_x].walkDown
            if(cord_y < 7 and self.board[cord_y+1][cord_x] == None):
                self.board[cord_y + 1][cord_x] = self.board[cord_y][cord_x]
            elif(cord_x > 0 and type(self.board[cord_y+1][cord_x]) is Tool):
                self.player.pickUp(self.board[cord_y+1][cord_x])
                self.board[cord_y+1][cord_x] = self.board[cord_y][cord_x]
            else:
                return False
        elif(direction == Direction.UP):
            self.board[cord_y][cord_x].sprite = self.board[cord_y][cord_x].walkUp
            if(cord_y > 0 and self.board[cord_y - 1][cord_x] == None):
                self.board[cord_y - 1][cord_x] = self.board[cord_y][cord_x]
            elif(cord_x > 0 and type(self.board[cord_y-1][cord_x]) is Tool):
                self.player.pickUp(self.board[cord_y-1][cord_x])
                self.board[cord_y-1][cord_x] = self.board[cord_y][cord_x]
            else:
                return False
        self.board[cord_y][cord_x] = None

    def getCordsOf(self, object):
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x == self.player):
                    return [index_x, index_y]

    def addObject(self, game_object, x, y):
        self.board[y][x] = game_object

    def addPlayer(self, player_object, x, y):
        self.board[y][x] = player_object
        self.player = player_object

    def renderSprites(self):
        self.window.blit(self.background, (0, 0))
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x != None):
                    sprite = pygame.image.load(x.sprite).convert_alpha()
                    self.window.blit(sprite, (DISPLACEMENT_X + index_x*SQUARE_SIZE,
                                              DISPLACEMENT_Y + index_y*SQUARE_SIZE))

    def close(self):
        self.run = False
        pygame.quit()
