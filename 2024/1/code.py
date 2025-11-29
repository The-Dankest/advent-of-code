from collections import Counter

a = []
b = []

with open("input.txt") as f:
    while True:
        line = f.readline()
        if line:
            x, y = map(int, line.split())
            a.append(x)
            b.append(y)
        else:
            break

counts = Counter(b)

total = 0
for x in a:
    total += (x * counts.get(x, 0))

print(total)
