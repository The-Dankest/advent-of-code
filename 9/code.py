line = input()

disk = []
count = 0
for i in range(len(line)):
    disk += ([-1 if i % 2 != 0 else count] * int(line[i]))
    count += i % 2

reverse = [x for x in disk[::-1] if x != -1]

print(reverse)

new = []
count = 0
for i in range(len(reverse)):
    if disk[i] == -1:
        new.append(reverse[count])
        count += 1
    else:
        new.append(disk[i])


# TODO: Checksum
checksum = 0
for i in range(len(new)):
    checksum += (i * new[i])

print(checksum)