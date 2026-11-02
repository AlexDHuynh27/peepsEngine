class Piece:
    def __init__(self, pieceType, colorIndex):
        self.pieceType = ['Frog', 'Turtle', 'Snake', 'Gator'][pieceType]
        self.color = [(255, 0, 0), (0, 0, 255), (212, 175, 55)][colorIndex] # red, blue, gold
        self.position = (1, 1)
        self.movementPattern = [self.frog, self.turtle, self.snake, self.gator][pieceType]
        self.tile = None

    def __str__(self):
        return f"{self.color} {self.pieceType}"

    def __repr__(self):
        return f"{self.color} {self.pieceType}"
    
    def move(self, board):
        self.movementPattern(board)

    def frog(self, board):
        return
    
    def turtle(self, board):
        return

    def snake(self, board):
        return

    def gator(self, board):
        return
