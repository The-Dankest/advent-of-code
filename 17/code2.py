ans = [2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0]

value = 0
for j in range(len(ans)):
    for i in range(8 ** (j + 1)):
        a = 8 * value + i

        output = []

        while True:
            b = a % 8
            b = b ^ 2
            c = a // (2 ** b)
            b = b ^ 3
            b = b ^ c
            output.append(b % 8)
            a = a // 8
            if a == 0:
                break
        
        print(output)
        print(ans[len(ans) - j - 1:])
        if ans[len(ans) - j - 1:] == output:
            value = 8 * value + i
            print(value)
            break

print(value)
