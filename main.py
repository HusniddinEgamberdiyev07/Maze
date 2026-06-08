import os
from src.grid import Grid
from src.display import Display
from src.generator import Generator

grid = Grid(7, 7)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(5, 5)

grid.set_player(1, 1)


def move(dx, dy):
    r, c = grid.player
    nr, nc = r + dx, c + dy

    # safety check: inside grid
    if nr < 0 or nr >= grid.rows or nc < 0 or nc >= grid.cols:
        return

    # wall check
    if grid.cells[nr][nc] != 0:
        grid.set_player(nr, nc)


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
        move(-1, 0)
    elif cmd == "s":
        move(1, 0)
    elif cmd == "a":
        move(0, -1)
    elif cmd == "d":
        move(0, 1)