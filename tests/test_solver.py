import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator
from src.solver import Solver


def setup_grid():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()
    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)
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


def test_bfs_shorter_or_equal_than_dfs():
    grid = setup_grid()
    solver = Solver(grid)

    bfs_path = solver.solve(method="bfs")
    dfs_path = solver.solve(method="dfs")

    assert len(bfs_path) <= len(dfs_path)


def test_invalid_method_raises_error():
    grid = setup_grid()
    solver = Solver(grid)

    try:
        solver.solve(method="xyz")
        assert False  # should not reach here
    except ValueError:
        assert True