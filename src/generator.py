import random


class Generator:
    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols

    def generate_recursive(self, density=1.0):
        # reset grid
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid.cells[r][c] = 0

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        def is_valid(r, c):
            return 0 < r < self.rows - 1 and 0 < c < self.cols - 1

        def carve(r, c):
            # density controls how often we carve
            if random.random() < min(1.0, density):
                self.grid.cells[r][c] = 1

        def dfs(r, c):
            visited[r][c] = True
            carve(r, c)

            random.shuffle(directions)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if is_valid(nr, nc) and not visited[nr][nc]:
                    wall_r = r + dr // 2
                    wall_c = c + dc // 2

                    carve(wall_r, wall_c)
                    dfs(nr, nc)

        dfs(1, 1)