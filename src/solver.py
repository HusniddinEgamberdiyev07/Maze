from heapq import heappush, heappop

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def heuristic(self, a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def solve(self):
        start = self.grid.start
        end = self.grid.end

        heap = []
        heappush(heap, (0, start))

        came_from = {}
        cost = {start: 0}

        while heap:
            _, current = heappop(heap)

            if current == end:
                break

            r, c = current

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                nxt = (nr, nc)

                if not (0 <= nr < self.grid.rows and 0 <= nc < self.grid.cols):
                    continue

                if self.grid.cells[nr][nc] == 0:
                    continue

                new_cost = cost[current] + 1

                if nxt not in cost or new_cost < cost[nxt]:
                    cost[nxt] = new_cost
                    priority = new_cost + self.heuristic(nxt, end)
                    heappush(heap, (priority, nxt))
                    came_from[nxt] = current

        # rebuild path
        if end not in came_from:
            return None

        path = []
        cur = end

        while cur != start:
            path.append(cur)
            cur = came_from[cur]

        path.append(start)
        path.reverse()

        # mark path
        for r, c in path:
            if (r, c) != start and (r, c) != end:
                self.grid.cells[r][c] = 2

        return path