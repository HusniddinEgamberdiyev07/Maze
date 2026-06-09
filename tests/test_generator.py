import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator


def test_generator_creates_paths():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    assert any(1 in row for row in grid.cells)


def test_generator_keeps_outer_walls():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    for col in range(grid.cols):
        assert grid.cells[0][col] == 0
        assert grid.cells[-1][col] == 0

    for row in range(grid.rows):
        assert grid.cells[row][0] == 0
        assert grid.cells[row][-1] == 0


def test_generator_has_open_and_walls():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    walls = sum(cell == 0 for row in grid.cells for cell in row)
    paths = sum(cell == 1 for row in grid.cells for cell in row)

    assert walls > 0
    assert paths > 0


def test_generator_density_variation():
    grid_low = Grid(9, 9)
    grid_high = Grid(9, 9)

    Generator(grid_low).generate_recursive(density=0.5)
    Generator(grid_high).generate_recursive(density=1.5)

    paths_low = sum(cell == 1 for row in grid_low.cells for cell in row)
    paths_high = sum(cell == 1 for row in grid_high.cells for cell in row)

    # high density should generally create more paths
    assert paths_high >= paths_low