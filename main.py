import os
from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.game import Game


grid = Grid(7, 7)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(5, 5)

grid.set_player(1, 1)

game = Game(grid)




while True:
    os.system("cls")  # Windows clear screen

    print(Display.render(grid))

    if grid.player == grid.end:
        print("🎉 YOU WIN!")
        break

    cmd = input("Move (WASD, Q=quit): ").lower()

    if cmd == "q":
        break
    elif cmd == "w":
        game.move_player(-1, 0)
    elif cmd == "s":
        game.move_player(1, 0)
    elif cmd == "a":
        game.move_player(0, -1)
    elif cmd == "d":
        game.move_player(0, 1)