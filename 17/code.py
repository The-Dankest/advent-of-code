ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

A = int(input().split()[2])
B = int(input().split()[2])
C = int(input().split()[2])
IP = 0
input()
program = [int(x) for x in input().replace("Program: ", "").split(',')]
out = []

while 0 <= IP < len(program):
    opcode = program[IP]
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: A,
        5: B,
        6: C,
        7: -1,
    }[program[IP + 1]]
    literal = program[IP + 1]
    
    if opcode == ADV:
        A = A // (2 ** combo)
    elif opcode == BXL:
        B = B ^ literal
    elif opcode == BST:
        B = combo % 8
    elif opcode == JNZ:
        if A != 0:
            IP = literal - 2
    elif opcode == BXC:
        B = B ^ C
    elif opcode == OUT:
        out.append(combo % 8)
    elif opcode == BDV:
        B = A // (2 ** combo)
    elif opcode == CDV:
        C = A // (2 ** combo)

    IP += 2

print(",".join([str(o) for o in out]))
