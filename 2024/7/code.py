from itertools import combinations_with_replacement, product

count = 0

while True:
    try:
        line = input()
        answer, operands = line.split(":")
        answer = int(answer)
        operands = [int(x) for x in operands.split()]
        for operators in product(["*", "+", "||"], repeat=len(operands) - 1):
            total = operands[0]
            for i, op in enumerate(operators):
                if op == "*":
                    total *= operands[i + 1]
                elif op == "+":
                    total += operands[i + 1]
                else:
                    total = int(str(total) + str(operands[i + 1]))
            if answer == total:
                count += answer
                break
    except EOFError:
        break

print(count)