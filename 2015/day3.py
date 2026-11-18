
fname = 'in.txt'
with open(fname, 'r') as f:
   line = f.readline().strip()

dic = {
        '>': [1,0],
        '^': [0,1],
        'v': [0,-1],
        '<': [-1,0]
        }

# coord_list = [[0,0]]
# visited = [[0,0]]
#part1
# for l in line:
#     direction = dic[l]
#     new_coord = [a + b for a, b in zip(coord_list[-1], direction)]
#     coord_list.append(new_coord)
#     if new_coord not in visited:
#         visited.append(new_coord)
#
# res1 = len(visited)
# print(res1)

#part2
santa = [[0,0]]
robo_santa = [[0,0]]
visited = [[0,0]]

for i in range(len(line)):
    direction = dic[line[i]]
    if i % 2 == 0:
        new_coord = [a + b for a,b in zip(santa[-1], direction)]
        santa.append(new_coord)
        if new_coord not in visited:
            visited.append(new_coord)
    else:
        new_coord = [a + b for a,b in zip(robo_santa[-1], direction)]
        robo_santa.append(new_coord)
        if new_coord not in visited:
            visited.append(new_coord)
res2 = len(visited)
print(res2)

