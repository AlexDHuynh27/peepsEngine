import pygame

class Tile:
    def __init__(self, x, y, absX, absY, radius, startingPieces, ):
        self.CORNER = False
        self.x = x
        self.y = y
        self.absX = absX
        self.absY = absY
        self.radius = radius
        self.pieces = startingPieces
        self.home = None
        self.playerOn = False

    def __str__(self):
        return "Tile"


    def draw(self, display):
        pygame.draw.circle(display, (255, 255, 255), (self.absX, self.absY), self.radius, width=0)
