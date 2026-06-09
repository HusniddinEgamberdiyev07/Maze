from collections import deque

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, method="bfs"):
        start = self.grid.start
        end = self.grid.end

        if method == "bfs":
            return self._bfs(start, end)
        elif method == "dfs":
            return self._dfs(start, end)
        else:
            raise ValueError("method must be 'bfs' or 'dfs'")

    # ---------------- BFS ----------------
    def _bfs(self, start, end):
        queue = deque([start])
        visited = set([start])
        parent = {}

        while queue:
            r, c = queue.popleft()

            if (r, c) == end:
                break

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if not self._valid(nr, nc, visited):
                    continue

                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

        return self._reconstruct(start, end, parent)

    # ---------------- DFS ----------------
    def _dfs(self, start, end):
        stack = [start]
        visited = set([start])
        parent = {}

        while stack:
            r, c = stack.pop()

            if (r, c) == end:
                break

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if not self._valid(nr, nc, visited):
                    continue

                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                stack.append((nr, nc))

        return self._reconstruct(start, end, parent)

    # ---------------- helpers ----------------
    def _valid(self, r, c, visited):
        return (
            0 <= r < self.grid.rows and
            0 <= c < self.grid.cols and
            self.grid.cells[r][c] != 0 and
            (r, c) not in visited
        )

    def _reconstruct(self, start, end, parent):
        if end not in parent:
            return None

        path = []
        cur = end

        while cur != start:
            path.append(cur)
            cur = parent[cur]

        path.append(start)
        path.reverse()

        # DO NOT paint full grid anymore
        self.grid.solution_path = set(path)

        return path