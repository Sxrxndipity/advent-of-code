import hashlib

#part1
key = "ckczppom"
i = 1
while (True):
    win = key + str(i)
    h = hashlib.md5(win.encode())
    res = h.hexdigest()
    if res[:5] == "00000":
        break
    i += 1
print(i)
#part2
# just add a 0 and turn 5 to 6
