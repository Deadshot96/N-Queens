import pygame
from Block import Block
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
        self.clock = None
        self.board = list()
        self.queenImg = None
        self.nQueens = NQUEENS
        self.size = 0

    def gui_init(self):
        
        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("N-Queen")
        self.win.fill(MIDBLACK)

        boardRect = self.x_off, self.y_off, self.boardWidth, self.boardHeight
        self.boardWin = self.win.subsurface(boardRect)

        self.font = pygame.font.SysFont('comicsansms', 40, True)
        title = self.font.render("N-Queen Backtracking", 1, GOLDENROD)
        w, h = title.get_size()
        blitPos = (self.width - w) // 2, (self.y_off - h) // 2
        self.win.blit(title, blitPos)

        self.board_init()

        pygame.display.update()

    def board_init(self):
        self.queenImg = pygame.image.load(QUEEN_IMGNAME)
        
        xOffset = (self.boardWidth % self.nQueens) // 2
        yOffset = (self.boardHeight % self.nQueens) // 2

        size = (self.boardWidth - xOffset) // self.nQueens
        
        # print(size)

        self.board = list()
        for row in range(self.nQueens):
            self.board.append(list())
            for col in range(self.nQueens):
                self.board[row].append(Block(row, col, size, xOffset, yOffset))

        self.queenImg = pygame.transform.scale(self.queenImg, (size // 2, size // 2))
    
    def draw_board(self):
        for row in self.board:
            for block in row:
                block.draw(self.boardWin)

        pygame.display.update()


    def run(self):
        self.gui_init()
        
        run = True
        while run:
            
            self.clock.tick(self.fps)
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
        
        self.quit()

    def quit(self):
        pygame.font.quit()
        pygame.quit()



if __name__ == "__main__":
    X = Board()
    X.run()