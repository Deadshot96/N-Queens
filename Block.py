import pygame

class Block:

    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.x = self.col * self.size
        self.y = self.row * self.size
    