class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = [
            [0 for _ in range(cols)]
            for _ in range(rows)
        ]

        self.start = None
        self.end = None

    def create_path(self, r, c):
        self.cells[r][c] = 1

    def mark_explored(self, r, c):
        self.cells[r][c] = 2

    def set_start(self, r, c):
        self.start = (r, c)

    def set_end(self, r, c):
        self.end = (r, c)