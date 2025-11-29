from sys import stdin
from functools import cache
from itertools import permutations

n_pad = {
    " ": (3, 0),
    "A": (3, 2),
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

d_pad = {
    "A": (0, 2),
    "^": (0, 1),
    " ": (0, 0),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

d_n_pad = {(x, y): (n_pad[x][0] - n_pad[y][0], n_pad[x][1] - n_pad[y][1]) for x in n_pad for y in n_pad}
d_d_pad = {(x, y): (d_pad[x][0] - d_pad[y][0], d_pad[x][1] - d_pad[y][1]) for x in d_pad for y in d_pad}

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

@cache
def d_transition(a, b):
    dy, dx = d_d_pad[(a, b)]
    possible = []
    chars = ("v" if dy > 0 else "^" ) * abs(dy) + (">" if dx > 0 else "<") * abs(dx)
    for perm in permutations(chars):
        loc = d_pad[a]
        valid = True
        for p in perm:
            loc = (loc[0] + dirs[p][0], loc[1] + dirs[p][1])
            if loc == d_pad[" "]:
                valid = False
                break
        if valid:
            possible.append("".join(perm))
    return min(possible, key=len)

@cache
def n_transition(a, b):
    dy, dx = d_n_pad[(a, b)]
    possible = []
    chars = ("v" if dy > 0 else "^" ) * abs(dy) + (">" if dx > 0 else "<") * abs(dx)
    for perm in permutations(chars):
        loc = n_pad[a]
        valid = True
        for p in perm:
            loc = (loc[0] + dirs[p][0], loc[1] + dirs[p][1])
            if loc == n_pad[" "]:
                valid = False
                break
        if valid:
            possible.append("".join(perm))
    return min(possible, key=len)

def n_pad_path(code):
    path = ""
    current_c = "A"
    for c in code:
        path += f"{n_transition(current_c, c)}A"
        current_c = c
    return path

def d_pad_path(code):
    path = ""
    current_c = "A"
    for c in code:
        path += f"{d_transition(current_c, c)}A"
        current_c = c
    return path

def get_total_path(code):
    return d_pad_path(d_pad_path(n_pad_path(code)))

total = 0

for line in [l.strip() for l in stdin.readlines()]:
    path = get_total_path(line)
    print(path)
    print(len(path), int(line[:3]))
    total += len(path) * int(line[:3])

print(total)
