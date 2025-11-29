from sys import stdin
from datetime import datetime

prog_start = datetime.now()

grid = [line.strip() for line in stdin.readlines()]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

start = (-1, -1)
end = (-1, -1)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)

scores = { (start, 0): 0}

q = [(start, 0, [start])]

finishes = {}

while len(q):
    cell, d, history = q.pop()
    og_score = scores[(cell, d)]
    for dir, ds in [(d, 1), ((d + 1) % 4, 1001), ((d + 3) % 4, 1001)]:
        new_x = dirs[dir][0] + cell[0]
        new_y = dirs[dir][1] + cell[1]
        cell_score = scores.get(((new_x, new_y), dir), None)
        if grid[new_y][new_x] != "#" and (not cell_score or cell_score >= og_score + ds):
            scores[((new_x, new_y), dir)] = og_score + ds
            new_history = [*history, (new_x, new_y)]
            q.append(((new_x, new_y), dir, new_history))
            if grid[new_y][new_x] == "E":
                if og_score + ds not in finishes:
                    finishes[og_score + ds] = []
                finishes[og_score + ds].append(new_history)
                
min_score = min(score for score in [scores.get((end, x)) for x in range(len(dirs))] if score is not None)

print(len(set(c for p in finishes[min_score] for c in p)))


print(datetime.now() - prog_start)
