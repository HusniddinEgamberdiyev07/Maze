import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator
from src.solver import Solver


def test_bfs_returns_valid_path():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="bfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_dfs_returns_valid_path():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="dfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_solver_path_is_connected():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="bfs")

    # every step must move only 1 cell
    for i in range(1, len(path)):
        r1, c1 = path[i - 1]
        r2, c2 = path[i]

        assert abs(r1 - r2) + abs(c1 - c2) == 1