import pygame

pygame.init()
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
display.fill('white')

if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("mouse clicked")