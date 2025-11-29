word = "MAS"

with open("input.txt") as file:
    lines = file.readlines()

sentry = len(word) - 1

count = 0

directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

good_corners = [
    "MMSS",
    "SMMS",
    "MSSM",
    "SSMM",
]

grid = []
for i in range(sentry):
    grid.append("." * ((len(lines[0]) - 1) + (sentry * 2)))
for line in lines:
    grid.append(f"{'.' * sentry}{line.strip()}{'.' * sentry}")
for i in range(sentry):
    grid.append("." * ((len(lines[0]) - 1) + (sentry * 2)))

for i in range(sentry , sentry + len(lines[0]) - 1):
    for j in range(sentry, sentry + len(lines)):
        if grid[j][i] == "A":
            corners = []
            for d in directions:
                corners.append(grid[j + d[0]][i + d[1]])
            if  "".join(corners) in good_corners:
                count += 1
print(count)
