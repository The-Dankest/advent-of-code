from functools import cache

@cache
def count_stones(stone, iters):
    if iters == 0:
        return 1
    elif stone == 0:
        return count_stones(1, iters - 1)
    elif len(str(stone)) % 2 == 0:
        string = str(stone)
        return count_stones(int(string[:len(string) // 2]), iters - 1) + count_stones(int(string[len(string) // 2:]), iters - 1)
    else:
        return count_stones(stone * 2024, iters - 1)

print(sum(count_stones(stone, 75) for stone in [int(_) for _ in input().split()]))
