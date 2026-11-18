fname = 'in.txt'
with open(fname, 'r') as f:
    line = f.readline().strip()
#part1
res1 = 0
for char in line:
    if char == '(':
        res1 += 1
    else:
        res1 -= 1

#part2
res2 = 0
for i in range(len(line)):
    if line[i] == '(':
        res2 += 1
    else:
        res2 -= 1

    if res2 == -1:
        res2 = i + 1
        break

print("result1: ",res1)
print("result2: ",res2)
