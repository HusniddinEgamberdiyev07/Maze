from collections import deque
import time

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, animate=False, delay=0.0):
        start = self.grid.start
        end = self.grid.end

        if start is None or end is None:
            return None

        queue = deque([start])
        visited = set()
        parent = {}

        while queue:
            r, c = queue.popleft()

            if (r, c) == end:
                path = []
                cur = end

                while cur != start:
                    path.append(cur)
                    cur = parent[cur]

                path.append(start)
                path.reverse()

                for pr, pc in path:
                    self.grid.cells[pr][pc] = 2

                return path

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if animate and self.grid.cells[r][c] == 1:
                self.grid.cells[r][c] = 3  # explored

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < self.grid.rows and
                    0 <= nc < self.grid.cols and
                    self.grid.cells[nr][nc] != 0 and
                    (nr, nc) not in visited
                ):
                    queue.append((nr, nc))
                    parent[(nr, nc)] = (r, c)

            if animate:
                time.sleep(delay)

        return None