from sys import stdin
from re import findall

text = "\n".join(stdin.readlines())

total = 0

do = True
for m in findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", text):
    if m == "don't()":
        do = False
    elif m == "do()":
        do = True
    elif "mul" in m and do:
        a, b = map(int, m[m.find("(") + 1:m.find(")")].split(","))
        total += a * b

print(total)