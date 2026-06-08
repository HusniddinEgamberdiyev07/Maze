import os
import time

from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game
from src.solver import Solver


grid = Grid(7, 7)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(5, 5)

grid.set_player(1, 1)

game = Game(grid)
solver = Solver(grid)


def draw():
    os.system("cls")
    print(Display.render(grid))


while True:
    draw()

    if grid.player == grid.end:
        print("🎉 YOU WIN!")
        break

    print("\nControls:")
    print("WASD = move")
    print("A = auto solve")
    print("Q = quit")

    cmd = input("Move: ").lower()

    if cmd == "q":
        break

    elif cmd == "w":
        game.move_player(-1, 0)

    elif cmd == "s":
        game.move_player(1, 0)

    elif cmd == "a":
        print("\n🤖 Solving...\n")
        time.sleep(0.5)
        solver.solve(animate=True, delay=0.05)
        input("\nPress Enter to continue...")

    elif cmd == "d":
        game.move_player(0, 1)