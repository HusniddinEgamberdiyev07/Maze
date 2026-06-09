import os
import time
from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game
from src.solver import Solver


def choose_level():
    print("Select difficulty:")
    print("1 - Easy (7x7)")
    print("2 - Medium (15x15)")
    print("3 - Hard (25x25)")

    choice = input("Choose level: ")

    if choice == "1":
        return Grid(7, 7)
    elif choice == "2":
        return Grid(15, 15)
    elif choice == "3":
        return Grid(25, 25)

    print("Invalid choice, defaulting to Easy")
    return Grid(7, 7)


grid = choose_level()

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

    elapsed = int(time.time() - start_time)

    print("=== MAZE GAME ===")
    print(f"Steps: {game.steps}")
    print(f"Time: {elapsed}s")
    print()

    print(Display.render(grid))


while True:
    draw()

    print("\nControls:")
    print("WASD = move")
    print("A = auto solve")
    print("Q = quit")

    if game.is_won():
        elapsed = int(time.time() - start_time)

        print("\n🎉 YOU WIN!")
        print(f"Steps: {game.steps}")
        print(f"Time: {elapsed}s")
        break

    cmd = input("Move: ").lower()

    if cmd == "q":
        break

    elif cmd == "w":
        game.move_player(-1, 0)

    elif cmd == "s":
        game.move_player(1, 0)

    elif cmd == "a":
        path = solver.solve()

        if not path:
            print("No path found!")
            input("Press Enter...")
            continue

        for r, c in path:
            grid.player = (r, c)

            draw()
            time.sleep(0.05)

        elapsed = int(time.time() - start_time)

        print("\n🎉 Auto-solve completed!")
        print(f"Steps: {game.steps}")
        print(f"Time: {elapsed}s")

        input("Press Enter to continue...")