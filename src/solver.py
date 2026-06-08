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

        queue = deque()
        visited = [[False] * cols for _ in range(rows)]
        parent = {}

        sr, sc = start
        er, ec = end

        queue.append((sr, sc))
        visited[sr][sc] = True
        parent[(sr, sc)] = None

        # BFS search
        while queue:
            r, c = queue.popleft()

            if (r, c) == (er, ec):
                break

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    not visited[nr][nc] and
                    self.grid.cells[nr][nc] != 0
                ):
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    parent[(nr, nc)] = (r, c)

        # reconstruct path
        node = (er, ec)

        while node in parent and parent[node] is not None:
            r, c = node
            if node != start and node != end:
                self.grid.cells[r][c] = 2
            node = parent[node]