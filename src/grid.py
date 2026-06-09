class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]

        self.start = None
        self.end = None
        self.player = None

        # for visualization only (NOT logic)
        self.solution_path = set()
        self.explored = set()

    def create_path(self, r, c):
        self.cells[r][c] = 1

    def mark_explored(self, r, c):
        self.explored.add((r, c))

    def set_start(self, r, c):
        self.start = (r, c)

    def set_end(self, r, c):
        self.end = (r, c)

    def reset_solver_state(self):
        self.solution_path.clear()
        self.explored.clear()