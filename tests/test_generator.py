from src.grid import Grid
from src.generator import Generator


def test_carve_single_cell():
    grid = Grid(3, 3)
    gen = Generator(grid)

    gen.carve(1, 1)

    assert grid.cells[1][1] == 1