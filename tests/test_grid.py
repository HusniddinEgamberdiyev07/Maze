import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid


def test_grid_size():
    grid = Grid(5, 5)

    assert grid.rows == 5
    assert grid.cols == 5


def test_grid_starts_with_walls():
    grid = Grid(3, 3)

    assert grid.cells == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]