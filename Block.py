import pygame
from pygame import Surface
from settings import *
from typing import Tuple
class Block:

    def __init__(self, row: int, col: int, size: int, xOff: int, yOff: int):
        self.row = row
        self.col = col
        self.size = size
        self.xOffset = xOff
        self.yOffset = yOff
        self.x = self.col * self.size + self.xOffset
        self.y = self.row * self.size + self.yOffset
        self.color = None
        self.occupied = False
        self.queenImg = None
        self.selected = False

        self.get_color()


    def draw(self, win: Surface):
        rect = (self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, rect, 0)

        if self.is_selected():
            rect = (self.x, self.y, self.size - 1, self.size - 1)
            pygame.draw.rect(win, SELECTED_COLOR, rect, 2)

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

    def get_color(self):
        if self.row % 2:
            self.color = COLORS[self.col % 2]
        else:
            self.color = COLORS[(self.col + 1) % 2]

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def is_selected(self) -> bool:
        return self.selected

    def get_dims(self) -> Tuple[int]:
        return self.row, self.col
