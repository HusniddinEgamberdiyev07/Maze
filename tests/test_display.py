import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.display import Display


def test_display_walls():

    grid = Grid(2, 2)

    expected = "##\n##"

    assert Display.render(grid) == expected