from collections import deque

class Solver:
    def __init__(self, grid):
        self.grid = grid

    # =========================
    # MAIN ENTRY
    # =========================
    def solve(self, method="bfs", animate=False, delay=0.01):
        if method == "bfs":
            return self.bfs(animate, delay)
        elif method == "dfs":
            return self.dfs(animate, delay)
        else:
            raise ValueError("Unknown method. Use 'bfs' or 'dfs'.")

    # =========================
    # BFS (shortest path)
    # =========================
    def bfs(self, animate=False, delay=0.01):
        start = self.grid.start
        end = self.grid.end

        queue = deque([start])
        visited = {start}
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

                if animate:
                    self.grid.cells[nr][nc] = 3  # explored

        return self._reconstruct(parent, start, end)

    # =========================
    # DFS (deep search)
    # =========================
    def dfs(self, animate=False, delay=0.01):
        start = self.grid.start
        end = self.grid.end

        stack = [start]
        visited = set()
        parent = {}

        while stack:
            r, c = stack.pop()

            if (r, c) == end:
                break

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if not self._valid(nr, nc, visited):
                    continue

                if (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c)

                stack.append((nr, nc))

                if animate:
                    self.grid.cells[nr][nc] = 3  # explored

        return self._reconstruct(parent, start, end)

    # =========================
    # HELPERS
    # =========================
    def _valid(self, r, c, visited):
        return (
            0 <= r < self.grid.rows and
            0 <= c < self.grid.cols and
            self.grid.cells[r][c] != 0 and
            (r, c) not in visited
        )

    def _reconstruct(self, parent, start, end):
        path = []
        cur = end

        while cur in parent:
            path.append(cur)
            cur = parent[cur]

        path.append(start)
        path.reverse()

        # mark final path in grid
        for r, c in path:
            if (r, c) != start and (r, c) != end:
                self.grid.cells[r][c] = 2

        return path if path and path[0] == start else None