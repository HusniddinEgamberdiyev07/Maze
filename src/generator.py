import random


class Generator:
    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols

    # =========================
    # PUBLIC API
    # =========================
    def generate_recursive(self, density=1.0):
        """
        density:
            0.5 → easier maze (more open)
            1.0 → normal maze
            1.5 → harder maze (more walls)
        """

        # 1. Fill everything with walls
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid.cells[r][c] = 0

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        # start point (always inside)
        start_r, start_c = 1, 1

        def is_valid(r, c):
            return 0 < r < self.rows - 1 and 0 < c < self.cols - 1

        def carve(r, c):
            self.grid.cells[r][c] = 1

        # =========================
        # DFS BACKTRACK MAZE
        # =========================
        def dfs(r, c):
            visited[r][c] = True
            carve(r, c)

            random.shuffle(directions)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if is_valid(nr, nc) and not visited[nr][nc]:

                    # carve wall between cells
                    wall_r = r + dr // 2
                    wall_c = c + dc // 2
                    carve(wall_r, wall_c)

                    dfs(nr, nc)

        dfs(start_r, start_c)

        # =========================
        # ADD EXTRA OPENINGS (for difficulty control)
        # =========================
        self._add_loops(density)

        # ensure outer walls
        self._enforce_boundaries()

    # =========================
    # EXTRA PATHS (controls difficulty)
    # =========================
    def _add_loops(self, density):
        extra_paths = int((self.rows * self.cols) * 0.05 * density)

        for _ in range(extra_paths):
            r = random.randint(1, self.rows - 2)
            c = random.randint(1, self.cols - 2)

            # open random wall into path
            if self.grid.cells[r][c] == 0:
                self.grid.cells[r][c] = 1

    # =========================
    # KEEP BORDER WALLS SAFE
    # =========================
    def _enforce_boundaries(self):
        for r in range(self.rows):
            self.grid.cells[r][0] = 0
            self.grid.cells[r][self.cols - 1] = 0

        for c in range(self.cols):
            self.grid.cells[0][c] = 0
            self.grid.cells[self.rows - 1][c] = 0