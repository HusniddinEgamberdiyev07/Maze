class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = [
            [0 for _ in range(cols)]
            for _ in range(rows)
        ]

    def create_path(self, row, col):
        self.cells[row][col] = 1

    def mark_explored(self, row, col):
        self.cells[row][col] = 2