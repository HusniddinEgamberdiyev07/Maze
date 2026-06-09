import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.solver import Solver


def setup_grid():
    grid = Grid(5, 5)

    # create simple open path maze
    for r in range(5):
        for c in range(5):
            grid.cells[r][c] = 1

    grid.set_start(0, 0)
    grid.set_end(4, 4)

    return grid


def test_bfs_solver_returns_path():
    grid = setup_grid()
    solver = Solver(grid)

    path = solver.solve(method="bfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_dfs_solver_returns_path():
    grid = setup_grid()
    solver = Solver(grid)

    path = solver.solve(method="dfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_solver_invalid_method():
    grid = setup_grid()
    solver = Solver(grid)

    try:
        solver.solve(method="random")
        assert False  # should not reach here
    except ValueError:
        assert True