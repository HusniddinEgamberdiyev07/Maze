import os
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
    else:
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


def draw():
    os.system("cls")  # Windows clear screen
    print(Display.render(grid))


while True:
    draw()

    print("\nControls:")
    print("WASD = move")
    print("A = auto solve")
    print("Q = quit")

    if grid.player == grid.end:
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
        print("\n🤖 Solving...\n")
        
        path = solver.solve(animate=True, delay=0.05)
        
        draw()
        
        if path:
            print("\n✅ Path found!")
        else:
            print("\n❌ No path found")
            
        input("\nPress Enter to continue...")
        
        # 🔥 RESET VISUALIZATION (important)
        for r in range(grid.rows):
            for c in range(grid.cols):
                if grid.cells[r][c] in (2, 3):
                    grid.cells[r][c] = 1