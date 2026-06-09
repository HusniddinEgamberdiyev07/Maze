import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.solver import Solver


def test_solver_finds_path():
    grid = Grid(5, 5)

    for r in range(5):
        for c in range(5):
            grid.create_path(r, c)

    grid.set_start(0, 0)
    grid.set_end(4, 4)

    solver = Solver(grid)

    path = solver.solve()

    assert path is not None
    assert len(path) > 0


def test_solver_marks_path():
    grid = Grid(5, 5)

    for r in range(5):
        for c in range(5):
            grid.create_path(r, c)

    grid.set_start(0, 0)
    grid.set_end(4, 4)

    solver = Solver(grid)

    path = solver.solve()

    assert path is not None

    marked = sum(
        cell == 2
        for row in grid.cells
        for cell in row
    )

    assert marked > 0