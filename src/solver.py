from collections import deque
import time

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, animate=False, delay=0.05):
        start = self.grid.start
        end = self.grid.end

        queue = deque([start])
        visited = set([start])
        parent = {}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            if (r, c) == end:
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < self.grid.rows and
                    0 <= nc < self.grid.cols and
                    self.grid.cells[nr][nc] != 0 and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

                    if animate:
                        self.grid.cells[nr][nc] = 3
                        time.sleep(delay)

        # reconstruct path
        path = []
        cur = end

        while cur in parent:
            path.append(cur)
            cur = parent[cur]

        path.append(start)
        path.reverse()

        for r, c in path:
            if (r, c) != self.grid.start and (r, c) != self.grid.end:
                self.grid.cells[r][c] = 2

        return path if path and path[0] == start else None