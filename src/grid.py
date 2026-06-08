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
        self.player = None

    def create_path(self, row, col):
        self.cells[row][col] = 1

    def mark_explored(self, row, col):
        self.cells[row][col] = 2

    def set_start(self, row, col):
        self.start = (row, col)

    def set_end(self, row, col):
        self.end = (row, col)

    def set_player(self, row, col):
        self.player = (row, col)