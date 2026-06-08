class Game:
    def __init__(self, grid):
        self.grid = grid
        self.player = grid.start

    def move_player(self, dr, dc):
        r, c = self.player
        nr, nc = r + dr, c + dc

        # boundary check
        if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
            return

        # wall check
        if self.grid.cells[nr][nc] == 0:
            return

        self.player = (nr, nc)

    def is_won(self):
        return self.player == self.grid.end