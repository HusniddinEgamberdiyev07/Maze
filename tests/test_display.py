import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.display import Display


def test_display_returns_string():
    grid = Grid(3, 3)

    grid.player = (1, 1)
    grid.set_start(1, 1)
    grid.set_end(2, 2)

    output = Display.render(grid)

    assert isinstance(output, str)
    assert len(output) > 0