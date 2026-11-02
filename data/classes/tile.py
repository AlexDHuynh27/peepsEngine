import pygame
import math
import random

class Tile:
    def __init__(self, x, y, absX, absY, radius, startingPieces):
        self.CORNER = False
        self.x = x
        self.y = y
        self.absX = absX
        self.absY = absY
        self.radius = radius
        self.pieces = startingPieces
        self.home = None
        self.playerOn = False
        self.piecesMoved = True
        self.pieceRadius = 20

    def __str__(self):
        return "Tile"


    def draw(self, display):
        if self.piecesMoved:
            pygame.draw.circle(display, (255, 255, 255), (self.absX, self.absY), self.radius, width=0)
            upperBound = self.radius
            lowerBound = -self.radius
            pieceCoords = self.generate_circles(len(self.pieces), self.pieceRadius, self.radius, self.absX, self.absY)
            for i in range(len(pieceCoords)):
                pygame.draw.circle(display, self.pieces[i].color, pieceCoords[i], self.pieceRadius, width=0)
            self.piecesMoved = False

    def generate_circles(self, n, r, R, cx=0.0, cy=0.0, max_attempts=100000, restarts=20, rng=None):
        rng = rng or random.Random()

        if n == 0:
            return []
        if r > R:
            raise ValueError("Small circles are bigger than the container.")
        if n * r * r > R * R:
            raise ValueError("Impossible: the circles' total area exceeds the container's.")

        min_dist_sq = (2 * r) ** 2
        max_center_dist = R - r      
        cell = 2 * r                 

        for _ in range(restarts):
            centres = []
            grid = {}               
            failed = False

            for _ in range(n):
                placed = False
                for _ in range(max_attempts):
                    # uniform random point in the allowed region
                    angle = rng.uniform(0, 2 * math.pi)
                    dist = max_center_dist * math.sqrt(rng.random())
                    x, y = dist * math.cos(angle), dist * math.sin(angle)

                    gx, gy = math.floor(x / cell), math.floor(y / cell)
                    overlaps = any(
                        (x - px) ** 2 + (y - py) ** 2 < min_dist_sq
                        for dx in (-1, 0, 1)
                        for dy in (-1, 0, 1)
                        for px, py in grid.get((gx + dx, gy + dy), ())
                    )
                    if not overlaps:
                        centres.append((x, y))
                        grid.setdefault((gx, gy), []).append((x, y))
                        placed = True
                        break

                if not placed:
                    failed = True
                    break

            if not failed:
                return [(cx + x, cy + y) for x, y in centres]

        raise RuntimeError(
            f"Couldn't fit {n} circles of radius {r} in radius {R}. "
            "Try fewer/smaller circles or a bigger container."
        )