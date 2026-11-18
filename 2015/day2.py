fname = 'in.txt'
with open(fname, 'r') as f:
   lines = [line.strip() for line in f if line.strip()]
#part1
def calculate_wrap(dimensions):
    dimensions = list(map(int,dimensions.split('x')))
    l,w,h = dimensions
    box_surface = 2*l*w + 2*w*h + 2*h*l
    dimensions.remove(max(dimensions))
    extra_paper = dimensions[0] * dimensions[1]
    res = box_surface + extra_paper
    return res

res1 = 0
for line in lines:
    res1 += calculate_wrap(line)
print("part1: ",res1)
#part2
def calculate_ribbon(dimensions):
    dimensions = list(map(int,dimensions.split('x')))
    l,w,h = dimensions
    bow = l*w*h
    dimensions.remove(max(dimensions))
    present = 2*(sum(dimensions))
    res = bow + present
    return res
res2 = 0
for line in lines:
    res2 += calculate_ribbon(line)
print("part2: ",res2)
