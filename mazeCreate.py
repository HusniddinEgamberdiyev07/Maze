from numpy import random as r

grid = r.choice([0,1], p=[0.5, 0.5], size=[5, 10])

print(grid)

def isMaze():
    if grid[0][0] != 0 and grid[len(grid)-1][len(grid[len(grid)-1])-1] != 0:
        solve()

def solve():
    pass