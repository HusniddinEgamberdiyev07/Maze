import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.game import Game


def test_player_moves_on_path():
    grid = Grid(3, 3)

    grid.create_path(1, 1)
    grid.create_path(1, 2)

    grid.set_start(1, 1)
    grid.set_end(1, 2)

    grid.player = (1, 1)

    game = Game(grid)

    game.move_player(0, 1)

    assert grid.player == (1, 2)


def test_player_cannot_move_through_wall():
    grid = Grid(3, 3)

    grid.create_path(1, 1)

    grid.set_start(1, 1)
    grid.player = (1, 1)

    game = Game(grid)

    game.move_player(0, 1)

    assert grid.player == (1, 1)


def test_player_reaches_end():
    grid = Grid(3, 3)

    grid.create_path(1, 1)
    grid.create_path(1, 2)

    grid.set_start(1, 1)
    grid.set_end(1, 2)

    grid.player = (1, 1)

    game = Game(grid)

    game.move_player(0, 1)

    assert game.is_won()