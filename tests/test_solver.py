import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator
from src.solver import Solver


def test_solver_marks_solution_path():
    grid = Grid(5, 5)
    gen = Generator(grid)

    gen.generate_recursive()

    grid.set_start(1, 1)
    grid.set_end(3, 3)

    solver = Solver(grid)
    solver.solve()

    # at least one solution path cell should be marked
    solution_cells = sum(
        cell == 2
        for row in grid.cells
        for cell in row
    )

    assert solution_cells > 0