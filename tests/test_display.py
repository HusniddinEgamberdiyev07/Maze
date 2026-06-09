import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.display import Display


def test_display_returns_string():
    grid = Grid(2, 2)

    grid.set_start(0, 0)
    grid.set_end(1, 1)
    grid.player = (0, 0)

    output = Display.render(grid)

    assert isinstance(output, str)
    assert len(output) > 0


def test_display_contains_player_symbol():
    grid = Grid(2, 2)
    grid.player = (0, 0)

    output = Display.render(grid)

    assert "P" in output


def test_display_contains_start_end():
    grid = Grid(2, 2)
    grid.set_start(0, 0)
    grid.set_end(1, 1)

    output = Display.render(grid)

    assert "S" in output
    assert "E" in output


def test_display_handles_solution_path():
    grid = Grid(3, 3)

    grid.solution_path = {(0, 1), (1, 1)}

    output = Display.render(grid)

    assert isinstance(output, str)