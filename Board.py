import pygame
from Block import Block
import random
from settings import *
from typing import Tuple

class Board:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.boardWidth = BOARD_WIDTH
        self.boardHeight = BOARD_HEIGHT
        self.x_off = X_OFFSET
        self.y_off = Y_OFFSET
        self.x_bOffset = 0
        self.y_bOffset = 0
        self.win = None
        self.boardWin = None
        self.fps = FPS
        self.font = None
        self.clock = None
        self.board = [[]]
        self.queenImg = None
        self.nQueens = 12
        self.size = 0

        # Variables for board selection
        self.selected_pos = None
        self.rowQueenFlags = list()
        self.fSlashQueenFlags = list()
        self.bSlashQueenFlags = list()
        self.flagsInitiated = False

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
        self.queenImg = pygame.image.load(QUEEN_IMGNAME).convert_alpha()
        
        self.x_bOffset = (self.boardWidth % self.nQueens) // 2
        self.y_bOffset = (self.boardHeight % self.nQueens) // 2

        self.size = (self.boardWidth - self.x_bOffset) // self.nQueens
        
        # print(size)

        self.board = list()
        for row in range(self.nQueens):
            self.board.append(list())
            for col in range(self.nQueens):
                self.board[row].append(Block(row, col, self.size, self.x_bOffset, self.y_bOffset))

        queenImgSize = int(self.size * 0.7)
        self.queenImg = pygame.transform.scale(self.queenImg, (queenImgSize, queenImgSize))
    
    def draw_board(self):
        self.boardWin.fill(MIDBLACK)
        for row in self.board:
            for block in row:
                block.draw(self.boardWin)

        pygame.display.update()

    def clear_board(self):
        for row in self.board:
            for block in row:
                block.clear()
        self.flags_init()

    def occupy_random(self):
        for row in self.board:
            for block in row:
                if random.random() > 0.5:
                    block.occupy(self.queenImg)

    def get_row_col(self, x: int, y: int) -> Tuple:
        x -= (self.x_off + self.x_bOffset)
        y -= (self.y_off + self.y_bOffset)

        return y // self.size, x // self.size

    def is_valid_pos(self, row: int, col: int) -> bool:
        return row in range(self.nQueens) and col in range(self.nQueens)

    def is_valid_queen_pos(self, row: int, col: int) -> bool:
        if not self.flagsInitiated:
            self.flags_init()
        
        rowFlag = self.rowQueenFlags[row]
        fSlashFlag = self.fSlashQueenFlags[row + col]
        bSlashFlag = self.bSlashQueenFlags[((self.nQueens - 1) - (row - col))]

        ans = rowFlag or fSlashFlag or bSlashFlag
        return not ans
        
    def flags_init(self):
        self.rowQueenFlags = [False] * self.nQueens
        self.fSlashQueenFlags = [False] * (2 * self.nQueens - 1)
        self.bSlashQueenFlags = [False] * (2 * self.nQueens - 1)  
        self.flagsInitiated = True

    def set_flags(self, row: int, col: int, flag: bool):
        self.rowQueenFlags[row] = flag
        self.fSlashQueenFlags[row + col] = flag
        self.bSlashQueenFlags[(self.nQueens - 1) - (row - col)] = flag

    def solve_gui(self, col: int) -> bool:
        if col == (self.nQueens):
            return True

        for row in range(self.nQueens):
            
            if self.is_valid_queen_pos(row, col):
                self.board[row][col].occupy(self.queenImg)
                self.set_flags(row, col, True)
                self.draw_board()
                pygame.time.delay(100)

                if self.solve_gui(col + 1):
                    return True
                
                self.board[row][col].clear()
                self.set_flags(row, col, False)
                self.draw_board()
                pygame.time.delay(100)


        return False

    def run(self):
        self.gui_init()
        # self.occupy_random()
        
        run = True
        while run:
            
            self.clock.tick(self.fps)
            self.draw_board()
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        self.clear_board()
                        self.solve_gui(0)
                        self.draw_board()
                        # for row in self.board:
                        #     for block in row:
                        #         if block.isOccupied() and random.random() < 0.5:
                        #             block.clear()

                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        if self.selected_pos:
                            self.selected_pos.occupy(self.queenImg)

                    if event.key == pygame.K_ESCAPE:
                        if self.selected_pos:
                            self.selected_pos.clear()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    row, col = self.get_row_col(x, y)

                    if self.is_valid_pos(row, col):
                        print(row, col, self.win.get_at(pos), sep = '\t')

                        if self.selected_pos:
                            self.selected_pos.deselect()

                        self.selected_pos = self.board[row][col]
                        self.selected_pos.select()
                
                    else:
                        if self.selected_pos:
                            self.selected_pos.deselect()
                            self.selected_pos = None

            pygame.display.update()
        
        self.quit()

    def quit(self):
        pygame.font.quit()
        pygame.quit()



if __name__ == "__main__":
    X = Board()
    X.run()