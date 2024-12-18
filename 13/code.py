from sys import stdin
from re import search
import numpy as np


pattern_button = r"X\+(\d+), Y\+(\d+)"
pattern_prize = r"X=(\d+), Y=(\d+)"

ax = -1
ay = -1
bx = -1
by = -1

totals = []

for line in [line.strip() for line in stdin.readlines()]:
    if line.startswith("Button A"):
        if m := search(pattern_button, line):
            ax, ay = [int(x) for x in m.groups()]
    elif line.startswith("Button B"):
        if m := search(pattern_button, line):
            bx, by = [int(x) for x in m.groups()]
    else:
        if m := search(pattern_prize, line):
            px, py = [int(x) for x in m.groups()]
            A = np.array([[ax, bx],
              [ay, by]])
            P = np.array([px, py])
            if np.linalg.det(A) != 0:
                a, b = np.linalg.solve(A, P)
                totals.append(3 * a + b)

print(sum(totals))
