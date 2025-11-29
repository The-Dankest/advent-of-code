from itertools import product
from sys import stdin

grid = [line.strip() for line in stdin.readlines()]

width = len(grid[0])
height = len(grid)

an = set()

towers = {}
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != ".":
            if cell not in towers:
                towers[cell] = []
            towers[cell].append((x, y))

print(towers)

for t in towers:
    for t1, t2 in product(towers[t], towers[t]):
        if t1 != t2:
            an.add(t1)
            dx = t2[0] - t1[0]
            dy = t2[1] - t1[1]
            x = t1[0] - dx
            y = t1[1] - dy
            while 0 <= x < width and 0 <= y < height:
                an.add((x, y))
                x -= dx
                y -= dy

print(len(an))
