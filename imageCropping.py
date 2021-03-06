import pygame
import os

def main():

    width = 642
    height = 214

    pieceWidth = pieceHeight = 107

    os.chdir(os.path.join(os.getcwd(), 'assets'))
    imgName = 'Pieces.png'

    img = pygame.transform.scale(pygame.image.load(imgName), (width, height))

    for i in range(6):
        for j in range(2):
            rect = (i * pieceWidth, j * pieceHeight, pieceWidth, pieceHeight)
            piece = img.subsurface(rect)

            pygame.image.save(piece, f'{i + j * 6}.png')


if __name__ == "__main__":
    main()