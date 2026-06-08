import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.grid import Grid
from src.generator import Generator


def test_generator_creates_some_paths():
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


def test_generator_is_not_fully_open():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    wall_count = sum(cell == 0 for row in grid.cells for cell in row)
    path_count = sum(cell == 1 for row in grid.cells for cell in row)

    assert wall_count > 0
    assert path_count > 0


def test_generator_has_reasonable_density():
    grid = Grid(7, 7)
    Generator(grid).generate_recursive()

    total = grid.rows * grid.cols
    paths = sum(cell == 1 for row in grid.cells for cell in row)

    # 20%–60% paths is realistic for small maze
    assert 0.2 * total < paths < 0.6 * total

from collections import deque

def test_maze_is_solvable():
    grid = Grid(7, 7)
    generator = Generator(grid)
    generator.generate_recursive()

    start = grid.start if grid.start else (1, 1)
    end = grid.end if grid.end else (5, 5)

    visited = set()
    queue = deque([start])

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            assert True
            return

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < grid.rows and
                0 <= nc < grid.cols and
                grid.cells[nr][nc] == 1
            ):
                queue.append((nr, nc))

    assert False, "Maze is not solvable" 