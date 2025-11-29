from sys import stdin
from PIL import Image
from pathlib import Path

Path.mkdir("test", exist_ok=True)

width = 101
height = 103


def get_pair(line: str):
    eq = line.find("=")
    comma = line.find(",")
    return int(line[eq + 1: comma]), int(line[comma + 1:])

def predict_pos(x, y, vx, vy, t):
    new_x = (x + (vx * t)) % width
    new_y = (y + (vy * t)) % height

    return (new_x, new_y)

robs = []
for line in stdin.readlines():
    p, v = line.strip().split()
    robs.append((get_pair(p), get_pair(v)))

for i in range(100000):
    image = Image.new('RGB', (width, height), 'white')
    for bot in robs:
        x, y = predict_pos(bot[0][0], bot[0][1], bot[1][0], bot[1][1], i)
        image.putpixel((x, y), (0, 0, 0))
    image.save(f"test/{i}.png")
