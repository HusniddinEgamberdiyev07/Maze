class Game:
    def __init__(self, grid):
        self.grid = grid
        self.steps = 0

    def move_player(self, dr, dc):
        r, c = self.grid.player
        nr, nc = r + dr, c + dc

        # boundary check
        if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
            return

        # wall check
        if self.grid.cells[nr][nc] == 0:
            return

        self.grid.player = (nr, nc)
        self.steps += 1

    def is_won(self):
        return self.grid.player == self.grid.end