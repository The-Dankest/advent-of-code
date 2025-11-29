# size = 7
# iters = 12
size = 71
iters = 2951

grid = [[0 for __ in range(size)] for _ in range(size)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = (0, 0)
end = (size - 1, size - 1)

for i in range(iters):
    x, y = [int(_) for _ in input().strip().split(",")]
    grid[y][x] = -1

queue = [start]

while queue:
    cell = queue.pop()
    distance = grid[cell[1]][cell[0]]
    for dx, dy in dirs:
        new_x = cell[0] + dx
        new_y = cell[1] + dy
        if 0 <= new_x < size and 0 <= new_y < size and (grid[new_y][new_x] == 0 or grid[new_y][new_x] > distance + 1):
            grid[new_y][new_x] = distance + 1
            queue.append((new_x, new_y))

print(grid[end[1]][end[0]])
