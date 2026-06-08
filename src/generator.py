class Generator:
    def __init__(self, grid):
        self.grid = grid

    def carve(self, row, col):
        self.grid.cells[row][col] = 1

    def carve_corridor(self, row, start_col, length):
        for col in range(start_col, start_col + length):
            self.grid.cells[row][col] = 1