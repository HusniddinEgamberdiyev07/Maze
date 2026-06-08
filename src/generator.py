import random

class Generator:
    def __init__(self, grid):
        self.grid = grid

    def carve(self, row, col):
        self.grid.cells[row][col] = 1

    def carve_corridor(self, row, start_col, length):
        for col in range(start_col, start_col + length):
            self.grid.cells[row][col] = 1

    def generate(self):
        rows = self.grid.rows
        cols = self.grid.cols

        # simple random walk (first version of maze)
        r, c = 1, 1
        self.grid.cells[r][c] = 1

        for _ in range(rows * cols):
            direction = random.choice([(0,1), (1,0), (0,-1), (-1,0)])

            nr = r + direction[0]
            nc = c + direction[1]

            if 0 < nr < rows-1 and 0 < nc < cols-1:
                self.grid.cells[nr][nc] = 1
                r, c = nr, nc