class Generator:
    def __init__(self, grid):
        self.grid = grid

    def carve(self, row, col):
        self.grid.cells[row][col] = 1