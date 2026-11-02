import pygame

class Tile:
    def __init__(self, x, y, radius, startingPieces, ):
        self.CORNER = corner
        self.x = x
        self.y = y
        self.radius = 50
        self.pieces = startingPieces
        self.home = None
        self.playerOn = False


    def draw(self, display):
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), self.radius, width=0)
