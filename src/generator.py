import random

class Generator:
    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols

    def carve(self, r, c):
        self.grid.cells[r][c] = 1

    def generate_recursive(self):
        visited = [[False] * self.cols for _ in range(self.rows)]

        def is_valid(r, c):
            return 0 < r < self.rows - 1 and 0 < c < self.cols - 1

        def get_neighbors(r, c):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            random.shuffle(directions)

            result = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and not visited[nr][nc]:
                    result.append((nr, nc))
            return result

        def dfs(r, c):
            visited[r][c] = True
            self.grid.cells[r][c] = 1

            for nr, nc in get_neighbors(r, c):
                if not visited[nr][nc]:
                    dfs(nr, nc)

        dfs(1, 1)

