from src.grid import Grid
from src.generator import Generator
from src.solver import Solver


def test_solver_bfs_returns_path():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="bfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_solver_dfs_returns_path():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="dfs")

    assert path is not None
    assert path[0] == grid.start
    assert path[-1] == grid.end


def test_solver_path_is_valid_length():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(grid.rows - 2, grid.cols - 2)

    solver = Solver(grid)
    path = solver.solve(method="bfs")

    assert len(path) > 2