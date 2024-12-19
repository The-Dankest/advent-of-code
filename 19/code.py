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
def is_valid(string):
    if string == "":
        return True
    for pattern in sorted_patterns[string[0]]:
        if match(pattern, string):
            if is_valid(string[len(pattern):]):
                return True
    return False

input()
count = 0

for line in stdin.readlines():
    line = line.strip()
    if is_valid(line):
        count += 1

print(count)
