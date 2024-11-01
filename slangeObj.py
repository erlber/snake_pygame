import pygame
import time

class Snake:
    def __init__(self, posX, posY, CELL_SIZE, color, screen):
        self.CELL_SIZE = CELL_SIZE
        self.height = CELL_SIZE
        self.width = CELL_SIZE
        self.posX = posX * CELL_SIZE
        self.posY = posY * CELL_SIZE
        self.dir = "r"
        self.color = color
        self.screen = screen
        self.speed = 200
        self.update = round(time.time() * 1000)
        self.body = [[self.posX, self.posY, self.width, self.height], [self.posX - 1 * CELL_SIZE, self.posY , self.width, self.height], [self.posX - 2 *CELL_SIZE, self.posY, self.width, self.height]]
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(self.screen, self.color, block)
        if(self.update < round(time.time() * 1000) - self.speed):
            if self.dir == "r":
                self.posX += 1 * self.CELL_SIZE
            elif self.dir == "l":
                self.posX -= 1 * self.CELL_SIZE
            
            self.update = round(time.time() * 1000)