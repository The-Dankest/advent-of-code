ans = [2, 4, 1, 2, 7, 5, 4, 7, 1, 3, 5, 5, 0, 3, 3, 0]

start = 35_184_372_088_832
end =  281_474_976_710_655

for i in range(start, end):
    a = i
    b = 0
    c = 0

    output = []

    while True:
        b = a % 8
        b = b ^ 2
        c = a // (2 ** b)
        b = b ^ c
        b = b ^ 3
        output.append(str(b % 8))
        a = a // 8
        if output[0] == 2:
            print(i)
            break
        # if a == 0:
        #     break

    # if ans == output:
    #     print(i)
    #     exit()
