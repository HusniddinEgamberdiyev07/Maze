import os
from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game

grid = Grid(7, 7)

Generator(grid).generate_recursive()

grid.set_start(1, 1)
grid.set_end(5, 5)

game = Game(grid)

game.player = grid.start


def move(dx, dy):
    game.move_player(dx, dy)


while True:
    os.system("cls")

    print(Display.render(grid, game))

    if game.is_won():
        print("🎉 YOU WIN!")
        break

    cmd = input("Move (WASD, Q=quit): ").lower()

    if cmd == "q":
        break
    elif cmd == "w":
        move(-1, 0)
    elif cmd == "s":
        move(1, 0)
    elif cmd == "a":
        move(0, -1)
    elif cmd == "d":
        move(0, 1)