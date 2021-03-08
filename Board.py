import pygame
from settings import *

class Board:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.boardWidth = BOARD_WIDTH
        self.boardHeight = BOARD_HEIGHT
        self.x_off = X_OFFSET
        self.y_off = Y_OFFSET
        self.win = None
        self.boardWin = None
        self.fps = FPS
        self.font = None

    def gui_init(self):
        
        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("N-Queen")
        self.win.fill(MIDBLACK)

        boardRect = self.x_off, self.y_off, self.boardWidth, self.boardHeight
        self.boardWin = self.win.subsurface(boardRect)

        self.font = pygame.font.SysFont('comicsansms', 40, True)
        title = self.font.render("N-Queens Backtracking", 1, GOLDENROD)
        w, h = title.get_size()
        blitPos = (self.width - w) // 2, (self.y_off - h) // 2
        self.win.blit(title, blitPos)

        pygame.display.update()





if __name__ == "__main__":
    X = Board()
    X.run()