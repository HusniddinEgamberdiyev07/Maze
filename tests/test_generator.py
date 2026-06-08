import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator


def test_generate_creates_some_paths():
    grid = Grid(5, 5)
    gen = Generator(grid)

    gen.generate_recursive()

    path_count = sum(
        cell == 1
        for row in grid.cells
        for cell in row
    )

    assert path_count > 1