from itertools import combinations_with_replacement, product

count = 0

while True:
    try:
        line = input()
        answer, operands = line.split(":")
        answer = int(answer)
        operands = [int(x) for x in operands.split()]
        for operators in product(["*", "+"], repeat=len(operands) - 1):
            print(operators)
            if answer == eval(str(operands[0]) + "".join([f"{operators[i]}{operands[i + 1]}" for i in range(len(operators))])):
                count += answer
                break
    except EOFError:
        break

print(count)