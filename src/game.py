class Game:
    def __init__(self, grid):
        self.grid = grid

    def move_player(self, dx, dy):
        r, c = self.grid.player
        nr, nc = r + dx, c + dy

        # boundary check
        if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
            return

        # wall check
        if self.grid.cells[nr][nc] == 0:
            return

        self.grid.set_player(nr, nc)