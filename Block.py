import pygame
from pygame import Surface
from settings import *

class Block:

    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.x = self.col * self.size
        self.y = self.row * self.size
        self.color = COLORS[(0 if self.row % 2 == 0 else 1 + self.col) % 8]
        self.occupied = False
        self.queenImg = None

    def draw(self, win: Surface):
        rect = (self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, rect, 0)

        if self.isOccupied():
            w, h = self.queenImg.get_size()
            blitPos = self.x + (self.size - w) // 2, self.y + (self.size - h) // 2
            win.blit(self.queenImg, blitPos)


    def isOccupied(self) -> bool:
        return self.occupied

    def occupy(self, img: Surface) -> None:
        self.occupied = True
        self.queenImg = img

    def clear(self):
        self.occupied = False
        self.queenImg = None