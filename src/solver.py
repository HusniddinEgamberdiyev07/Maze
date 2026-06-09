from collections import deque

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, method="bfs"):
        start = self.grid.start
        end = self.grid.end

        if method == "dfs":
            return self._dfs(start, end)
        return self._bfs(start, end)

    def _bfs(self, start, end):
        queue = deque([start])
        visited = set([start])
        parent = {}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        found = False

        while queue:
            r, c = queue.popleft()

            if (r, c) == end:
                found = True
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
                    continue

                if self.grid.cells[nr][nc] == 0:
                    continue

                if (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

        return self._reconstruct(parent, start, end) if found else None

    def _dfs(self, start, end):
        stack = [start]
        visited = set([start])
        parent = {}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        found = False

        while stack:
            r, c = stack.pop()

            if (r, c) == end:
                found = True
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
                    continue

                if self.grid.cells[nr][nc] == 0:
                    continue

                if (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                stack.append((nr, nc))

        return self._reconstruct(parent, start, end) if found else None

    def _reconstruct(self, parent, start, end):
        path = []
        cur = end

        while cur != start:
            path.append(cur)
            cur = parent.get(cur)

            if cur is None:
                return None

        path.append(start)
        path.reverse()

        # ONLY mark final path (important fix)
        for r, c in path:
            if (r, c) != start and (r, c) != end:
                self.grid.cells[r][c] = 2

        return path