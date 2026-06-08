from collections import deque

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        start = self.grid.start
        end = self.grid.end

        if not start or not end:
            return

        rows = self.grid.rows
        cols = self.grid.cols

        visited = [[False] * cols for _ in range(rows)]
        queue = deque()

        sr, sc = start
        er, ec = end

        queue.append((sr, sc))
        visited[sr][sc] = True

        while queue:
            r, c = queue.popleft()

            if (r, c) == (er, ec):
                return True

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    not visited[nr][nc] and
                    self.grid.cells[nr][nc] != 0
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return False