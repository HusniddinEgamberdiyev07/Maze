import os
import time
from collections import deque

from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game
from src.solver import Solver


# =========================
# CONFIG ENGINE
# =========================
def config():
    print("\n=== MAIN CONFIGURATION ENGINE ===")
    print("|-----------------------------|")

    width = input("Enter maze width (odd number recommended): ")
    height = input("Enter maze height: ")

    try:
        width = int(width)
        height = int(height)
    except:
        print("Invalid input, defaulting to 15x15")
        width, height = 15, 15

    print("\nChoose solver method:")
    print("1 - BFS (shortest path)")
    print("2 - DFS (deep search)")

    choice = input("Selection: ")

    method = "bfs"
    if choice == "2":
        method = "dfs"

    return width, height, method


# =========================
# INIT
# =========================
w, h, method = config()

grid = Grid(h, w)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(grid.rows - 2, grid.cols - 2)
grid.player = (1, 1)

game = Game(grid)
solver = Solver(grid)


start_time = time.time()


# =========================
# DRAW FUNCTION
# =========================
def draw():
    os.system("cls" if os.name == "nt" else "clear")

    elapsed = int(time.time() - start_time)

    print("=== MAZE GAME ===")
    print(f"Solver: {method.upper()}")
    print(f"Steps: {game.steps}")
    print(f"Time: {elapsed}s\n")

    print(Display.render(grid))


# =========================
# BFS (manual animation)
# =========================
def bfs_solve():
    start = grid.start
    end = grid.end

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            break

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < grid.rows and
                0 <= nc < grid.cols and
                grid.cells[nr][nc] != 0 and
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

                grid.cells[nr][nc] = 3  # explored

                draw()
                time.sleep(0.01)

    # rebuild path
    path = []
    cur = end

    while cur in parent:
        path.append(cur)
        cur = parent[cur]

    path.append(start)
    path.reverse()

    return path


# =========================
# DFS (simple version)
# =========================
def dfs_solve():
    stack = [grid.start]
    visited = set()
    parent = {}

    while stack:
        r, c = stack.pop()

        if (r, c) == grid.end:
            break

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < grid.rows and
                0 <= nc < grid.cols and
                grid.cells[nr][nc] != 0 and
                (nr, nc) not in visited
            ):
                parent[(nr, nc)] = (r, c)
                stack.append((nr, nc))

                grid.cells[nr][nc] = 3

                draw()
                time.sleep(0.01)

    # rebuild path
    path = []
    cur = grid.end

    while cur in parent:
        path.append(cur)
        cur = parent[cur]

    path.append(grid.start)
    path.reverse()

    return path


# =========================
# MAIN LOOP
# =========================
while True:
    draw()

    print("\nControls:")
    print("WASD = move")
    print("A = auto solve")
    print("Q = quit")

    if game.is_won():
        print("\n🎉 YOU WIN!")
        break

    cmd = input("Move: ").lower()

    if cmd == "q":
        break

    elif cmd == "w":
        game.move_player(-1, 0)

    elif cmd == "s":
        game.move_player(1, 0)

    elif cmd == "a":

        if method == "bfs":
            path = bfs_solve()
        else:
            path = dfs_solve()

        if not path:
            print("No path found!")
            input("Press Enter...")
            continue

        for r, c in path:
            grid.player = (r, c)
            draw()
            time.sleep(0.03)

        print("\n🎉 AUTO SOLVED!")
        input("Press Enter...")