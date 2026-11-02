class Piece:
    def __init__(self, pieceType, colorIndex):
        self.pieceType = ['Frog', 'Turtle', 'Snake', 'Gator'][pieceType]
        self.color = [(255, 0, 0), (0, 0, 255), (212, 175, 55)][colorIndex] # red, blue, gold
        self.position = (1, 1)
        self.movementPattern = [self.frog, self.turtle, self.snake, self.gator][pieceType]


    def __str__(self):
        return f"{self.color} {self.pieceType}"

    def __repr__(self):
        return f"{self.color} {self.pieceType}"
    
    def move(self, Board):
        self.movementPattern(Board)
