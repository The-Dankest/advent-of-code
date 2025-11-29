from sys import stdin
from functools import reduce
from operator import mul

# width = 11
# height = 7
width = 101
height = 103

time = 100


def get_pair(line: str):
    eq = line.find("=")
    comma = line.find(",")
    return int(line[eq + 1: comma]), int(line[comma + 1:])

def predict_pos(x, y, vx, vy, t):
    new_x = (x + (vx * t)) % width
    new_y = (y + (vy * t)) % height

    center_x = width // 2
    center_y = height // 2
    if new_x == center_x or new_y == center_y:
        return 0
    if new_x < center_x:
        if new_y < center_y:
            return 1
        else:
            return 2
    else:
        if new_y < center_y:
            return 3
        else:
            return 4

counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
}
for line in stdin.readlines():
    p, v = line.strip().split()
    px, py = get_pair(p)
    vx, vy = get_pair(v)
    quad = predict_pos(px, py, vx, vy, time)
    counts[quad] = counts[quad] + 1

print(counts)

del counts[0]
print(reduce(mul, counts.values()))
