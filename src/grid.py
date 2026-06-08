class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = [
            [0 for _ in range(cols)]
            for _ in range(rows)
        ]