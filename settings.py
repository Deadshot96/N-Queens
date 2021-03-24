import os

FPS = 60
WIDTH = 750
HEIGHT = 660
BOARD_WIDTH = 560
BOARD_HEIGHT = 560
X_OFFSET = (WIDTH - BOARD_WIDTH) // 4
Y_OFFSET = int((HEIGHT - BOARD_HEIGHT) * 0.8)
SPRITE_IMGNAME = 'Pieces.png'
ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
QUEEN_IMGNAME = os.path.join(ASSETS_DIR, '7.png')
QUEEN_IMGWIDTH = 50
QUEEN_IMGHEIGHT = 50
NOVAJOWHITE = (255, 222, 173)
PERU = (205, 133, 63)
COLORS = [PERU, NOVAJOWHITE]
MIDBLACK = (51, 51, 51)
GOLDENROD = (218, 165, 32)
SELECTED_COLOR = (255, 68, 51)
NQUEENS = 8
BUTTON_FONT = 'consolas'
BUTTON_FONT_SIZE = 20
BUTTON_PRESSED = 'button_p.png'
BUTTON_UNPRESS = 'button_up.png'
WHITE = (240, 240, 240)
BUTTON_LABEL_COLOR = WHITE
BUTTON_LABEL_HOVER_COLOR = PERU