from src.grid import Grid
from src.display import Display
from src.generator import Generator
from src.solver import Solver

grid = Grid(7, 7)

gen = Generator(grid)
gen.generate_recursive()

grid.set_start(1, 1)
grid.set_end(5, 5)

solver = Solver(grid)
solver.solve()

print(Display.render(grid))