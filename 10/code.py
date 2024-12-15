from sys import stdin

grid = [line.strip() for line in stdin.readlines()]

adj = [(-1, 0), (0, -1), (1, 0), (0, 1)]

width = len(grid[0])
height = len(grid)

starts = []
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "0":
            starts.append((x, y))

def find_path_count(x, y, count):
    if count == 9:
        return 1
    total = 0
    for next in adj:
        next_x = next[0] + x
        next_y = next[1] + y
        if 0 <= next_x < width and 0 <= next_y < height and grid[next_y][next_x] == str(count + 1):
            total += find_path_count(next_x, next_y, count + 1)
    return total

counts = [find_path_count(x, y, 0) for x, y in starts]
print(counts)
print(sum(counts))
