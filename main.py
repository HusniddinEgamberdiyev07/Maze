import os
import time

from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game
from src.solver import Solver


def choose_config():
    print("=== MAIN CONFIGURATION ENGINE ===")
    width = int(input("Enter maze width: "))
    height = int(input("Enter maze height: "))

    print("\nChoose solver method:")
    print("1 - BFS (shortest path)")
    print("2 - DFS (deep search)")

    choice = input("Choice: ")

    method = "bfs" if choice == "1" else "dfs"

    return width, height, method


w, h, method = choose_config()

grid = Grid(h, w)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(grid.rows - 2, grid.cols - 2)
grid.player = (1, 1)

game = Game(grid)
solver = Solver(grid)

start_time = time.time()


def draw():
    os.system("cls" if os.name == "nt" else "clear")
    print(Display.render(grid))


while True:
    draw()

    print(f"\nSolver: {method.upper()}")
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
        path = solver.solve(method=method)

        if not path:
            print("No path found!")
            input("Enter...")
            continue

        for r, c in path:
            grid.player = (r, c)
            draw()
            time.sleep(0.05)

        input("\nSolved! Press Enter...")