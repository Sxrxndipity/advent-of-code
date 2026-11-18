import re

fname = 'in.txt'
with open(fname, 'r') as f:
   lines = [line.strip() for line in f if line.strip()]

#part1
# def isNiceString(s):
#     return (
#         len(re.findall(r"[aeiou]", s)) >= 3
#         and bool(re.search(r"([a-z])\1", s))
#         and not re.search(r"ab|cd|pq|xy", s)
#     )
#
# res1 = 0
# for line in lines:
#     if isNiceString(line):
#         res1 += 1
# print(res1)
#part2
def isNiceString(x):
    return (
        bool(re.search(r"([a-z])[a-z]\1",x))
        and bool(re.search(r"([a-z]{2}).*\1",x))
    )

res2 = 0
for line in lines:
    if isNiceString(line):
        res2 += 1
print(res2)

