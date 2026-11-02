import numpy as np
import random
from data.classes.piece import Piece
from data.classes.tile import Tile


class Board:
    def __init__(self, length, players):
        self.width = length
        self.height = length
        self.tile_radius = (length / 5 - 20) // 2
        self.turnOrder = random.shuffle(players)
        self.meatstick = (1, 1)
        self.shack = (1,1)
        self.star = (3,3)

        #Drawing Related
        self.tileDistance = length % (4 *(self.tile_radius * 2)) # 50 is the radius change this



        # Everything Board Logic Related
        self.tileAllocation = [
            [3, 3, 3], 
            [3, 3, 3], 
            [3, 3, 3], 
            [1, 1, 1],
        ]
        # frog
        # turtle
        # snake
        # gator
        # r, b, y
        
        self.config =[
            ['fs', 'ft', 'ts', ''],
            ['ft', 'gg', 'ss', 'ts'],
            ['fs','fs','ff','tf'],
            ['tf','ts','tg','ts'],
        ]
        self.grid = self.generateTiles()
        self.tileBoard = [[],[],[],[]]
        for i in range(4):
            for j in range(4):
                self.tileBoard[i].append(Tile(
                    i, 
                    j, 
                    length/5 * (i+1), 
                    length/5 * (j+1), 
                    self.tile_radius,
                    self.grid[i][j]
                    )) 

    
    def __str__(self):
        s = ''
        for row in self.grid:
            s += f"{row} \n"
        return s

    def __repr__(self):
        return "The Board"

    def generateTiles(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        configuration = ''
        pieceType = 0
        tilePieces = []
        for i in range(4):
            for j in range(4):
                tilePieces = []
                configuration = self.config[i][j]
                for char in configuration:
                    if char == 'f':
                        pieceType = 0
                    elif char == 't':
                        pieceType = 1
                    elif char == 's':
                        pieceType = 2
                    else:
                        pieceType = 3
                    tilePieces.append(Piece(pieceType, self.chooseColor(pieceType)))
                board[i][j] = tilePieces

        return board

    def chooseColor(self, pieceType):
        selectionBase = self.tileAllocation[pieceType]
        non_zero_indices = np.nonzero(selectionBase)[0]
        color_index = random.choice(non_zero_indices)
        self.tileAllocation[pieceType][color_index] = self.tileAllocation[pieceType][color_index] - 1

        return color_index

    def draw(self, display):
        for tileRow in self.tileBoard:
            for tile in tileRow:
                
                tile.draw(display)

        return


                        
                


