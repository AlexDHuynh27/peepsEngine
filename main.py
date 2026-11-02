import pygame
from data.classes.board import Board

pygame.init()
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(600, ['hi', 'forest'])

def draw(display):
    board.draw(display)
    pygame.display.update()

    
if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for tileRow in board.tileBoard:
                        for tile in tileRow:
                            print(f"{tile.absX}, {tile.absY}")
                    print("mouse clicked")
        draw(screen)