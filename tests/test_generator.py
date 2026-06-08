import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator


def test_carve_corridor():
    grid = Grid(3, 3)
    gen = Generator(grid)

    gen.carve_corridor(1, 0, 3)

    assert grid.cells[1][0] == 1
    assert grid.cells[1][1] == 1
    assert grid.cells[1][2] == 1