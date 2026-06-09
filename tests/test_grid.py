import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid


def test_grid_size():
    grid = Grid(5, 5)
    assert grid.rows == 5
    assert grid.cols == 5


def test_grid_initial_walls():
    grid = Grid(3, 3)

    for row in grid.cells:
        for cell in row:
            assert cell == 0


def test_create_path():
    grid = Grid(3, 3)
    grid.create_path(1, 1)

    assert grid.cells[1][1] == 1


def test_set_start():
    grid = Grid(3, 3)
    grid.set_start(1, 1)

    assert grid.start == (1, 1)


def test_set_end():
    grid = Grid(3, 3)
    grid.set_end(2, 2)

    assert grid.end == (2, 2)


def test_player_can_be_set():
    grid = Grid(3, 3)
    grid.player = (1, 1)

    assert grid.player == (1, 1)


def test_solver_state_reset():
    grid = Grid(3, 3)
    grid.solution_path.add((1, 1))
    grid.explored.add((1, 2))

    grid.reset_solver_state()

    assert len(grid.solution_path) == 0
    assert len(grid.explored) == 0