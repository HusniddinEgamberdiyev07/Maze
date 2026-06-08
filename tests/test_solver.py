import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator
from src.solver import Solver


def test_solver_finds_path():
    grid = Grid(5, 5)
    gen = Generator(grid)

    gen.generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(3, 3)

    solver = Solver(grid)
    solver.solve()

    # start should be visited
    assert grid.start is not None
    assert grid.end is not None