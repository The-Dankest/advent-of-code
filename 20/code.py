from sys import stdin
grid = [list(line.strip()) for line in stdin.readlines()]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cheat_size = 100
cheat_length = 20

width = len(grid[0])
height = len(grid)

start = (-1, -1)
end = (-1, -1)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)

print(start, end)

path = [start]
grid[start[1]][start[0]] = 0

cheat_count = 0

while True:
    x, y = path[-1]
    if (x, y) == end:
        break
    for dx, dy in dirs:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < width and 0 <= new_y < height and grid[new_y][new_x] != "#" and not isinstance(grid[new_y][new_x], int):
            grid[new_y][new_x] = len(path)
            path.append((new_x, new_y))
            break

for cx, cy in path:
    for i in range(-cheat_length, cheat_length + 1):
        for j in range(-1 * (cheat_length - abs(i)), cheat_length - abs(i) + 1):
            d = abs(i) + abs(j)
            if d < 2 or d > cheat_length:
                continue
            p2 = cx + i, cy + j
            if not (0 <= cx + i < width) or not (0 <= cy + j < height) or not isinstance(grid[cy + j][cx + i], int):
                continue
            if grid[cy + j][cx + i] - grid[cy][cx] - d < cheat_size:
                continue
            cheat_count += 1
print(cheat_count)