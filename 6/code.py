from sys import stdin

grid = [list(line.strip()) for line in stdin.readlines()]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
position_count = 0

pos = (-1, -1)
for i, row in enumerate(grid):
    if "^" in row:
        j = row.index("^")
        pos = (i, j)
        row[j] = "X"
        break

print(pos)

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

while in_grid(pos[0], pos[1]):
    while True:
        next_pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        if in_grid(next_pos[0], next_pos[1]) and grid[next_pos[0]][next_pos[1]] == "#":
            dir = (dir + 1) % len(directions)
            continue
        break
    pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
    if in_grid(pos[0], pos[1]):
        next_pos = (pos[0] + directions[(dir + 1) % len(directions)][0], pos[1] + directions[(dir + 1) % len(directions)][1])
        if in_grid(next_pos[0], next_pos[1]) and grid[next_pos[0]][next_pos[1]] == "X":
            position_count += 1
        grid[pos[0]][pos[1]] = "X"

for row in grid:
    print("".join(row))

print(position_count)