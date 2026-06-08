import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator


def test_generator_creates_some_paths():
    grid = Grid(7, 7)

    generator = Generator(grid)
    generator.generate_recursive()

    path_count = 0

    for row in grid.cells:
        for cell in row:
            if cell == 1:
                path_count += 1

    assert path_count > 0

def test_generator_creates_starting_path():
    grid = Grid(7, 7)

    generator = Generator(grid)
    generator.generate_recursive()

    assert grid.cells[1][1] == 1

def test_generator_creates_vertical_path():
    grid = Grid(7, 7)

    generator = Generator(grid)
    generator.generate_recursive()

    assert grid.cells[2][1] == 1

def test_generator_keeps_outer_walls():
    grid = Grid(7, 7)

    generator = Generator(grid)
    generator.generate_recursive()

    for col in range(grid.cols):
        assert grid.cells[0][col] == 0
        assert grid.cells[grid.rows - 1][col] == 0

    for row in range(grid.rows):
        assert grid.cells[row][0] == 0
        assert grid.cells[row][grid.cols - 1] == 0