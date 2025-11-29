count = 0

with open("input.txt") as f:
    while True:
        line = f.readline()
        if line:
            levels = list(map(int, line.split()))
            
            for j in range(len(levels)):
                new_levels = levels[:j] + levels[j + 1:]
                deltas = []
                for i in range(len(new_levels) - 1):
                    deltas.append(new_levels[i] - new_levels[i + 1])
                if all([x > 0 and x <= 3 for x in deltas]) or all([x < 0 and x >= -3 for x in deltas]):
                    count += 1
                    break

        else:
            break

print(count)
