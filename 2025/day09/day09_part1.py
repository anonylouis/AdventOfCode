#!/usr/bin/python3
 
f = open('input.txt')

tiles = [list(map(int, line[:-1].split(','))) for line in f.readlines()]
n = len(tiles)

areas = []
for i in range(n) :
    for j in range(i + 1, n) :
        a, b = tiles[i], tiles[j]
        areas.append([(abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1), i, j])

areas.sort()

print(areas[-1][0])
