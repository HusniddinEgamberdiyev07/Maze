from src.grid import Grid
from src.generator import Generator


def test_generator_creates_paths():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    # at least some paths must exist
    assert any(1 in row for row in grid.cells)


def test_generator_keeps_boundaries():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    # outer walls must always remain walls
    for c in range(grid.cols):
        assert grid.cells[0][c] == 0
        assert grid.cells[-1][c] == 0

    for r in range(grid.rows):
        assert grid.cells[r][0] == 0
        assert grid.cells[r][-1] == 0


def test_generator_has_mixture_of_walls_and_paths():
    grid = Grid(9, 9)
    Generator(grid).generate_recursive()

    walls = sum(cell == 0 for row in grid.cells for cell in row)
    paths = sum(cell == 1 for row in grid.cells for cell in row)

    assert walls > 0
    assert paths > 0


def test_generator_density_variation():
    grid1 = Grid(9, 9)
    grid2 = Grid(9, 9)

    Generator(grid1).generate_recursive(density=0.5)
    Generator(grid2).generate_recursive(density=1.5)

    paths1 = sum(cell == 1 for row in grid1.cells for cell in row)
    paths2 = sum(cell == 1 for row in grid2.cells for cell in row)

    # higher density should create more openings
    assert paths2 >= paths1