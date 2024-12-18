line = input()

disk = []
count = 0
for i in range(len(line)):
    disk.append([-1 if i % 2 != 0 else count] * int(line[i]))
    count += i % 2

i = len(disk) - 1
while i > 0:
    if len(disk[i]) and disk[i][0] > 0:
        for j in range(i):
            if len(disk[j]) >= len(disk[i]) and disk[j][0] == -1:
                og = disk[i][::]
                disk[j] = [-1] * (len(disk[j]) - len(disk[i]))
                disk[i] = [-1] * len(disk[i])
                disk.insert(j, og)
                i += 1
                break
    i -= 1

checksum = 0
new_disk = [x for y in disk for x in y]
for i in range(len(new_disk)):
    checksum += (i * (max(new_disk[i], 0)))

print(checksum)