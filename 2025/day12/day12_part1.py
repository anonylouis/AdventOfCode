#!/usr/bin/python3

lines = open('input.txt').readlines()

shapes = []
regions = []

i = 0
while i < len(lines) :
    if lines[i][1] == ':' :
        shape = []
        i += 1
        while lines[i] != '\n' :
            shape.append(lines[i][:-1])
            i += 1
        shapes.append(shape)

    elif 'x' in lines[i] :
        region = lines[i][:-1].split(': ')
        region[0] = list(map(int, region[0].split('x')))
        region[1] = list(map(int, region[1].split()))
        regions.append(region)
    i += 1

s = 0

for region in regions :
    dim, presents = region
    totalTilesNeeded = 0
    for i in range(len(shapes)) :
        totalTilesNeeded += presents[i] * (''.join(shapes[i])).count('#')
    totalArea = dim[0] * dim[1]
    if (totalTilesNeeded <= totalArea) :
        s += 1

print(s)