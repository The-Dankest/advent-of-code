from functools import cache
from re import match
from sys import setrecursionlimit, stdin

patterns = [pattern.strip() for pattern in input().split(",")]
sorted_patterns = {
    "w": [pattern for pattern in patterns if pattern[0] == "w"],
    "r": [pattern for pattern in patterns if pattern[0] == "r"],
    "u": [pattern for pattern in patterns if pattern[0] == "u"],
    "b": [pattern for pattern in patterns if pattern[0] == "b"],
    "g": [pattern for pattern in patterns if pattern[0] == "g"],
}

@cache
def count(string):
    if string == "":
        return 1
    total = 0
    for pattern in sorted_patterns[string[0]]:
        if match(pattern, string):
            total += count(string[len(pattern):])
    return total

input()
total = 0

for line in stdin.readlines():
    line = line.strip()
    total += count(line)

print(total)
