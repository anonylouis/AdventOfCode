#!/usr/bin/python3

f = open('input.txt')
map = [list(line[:-1].replace('S', '|')) for line in f.readlines()]

n, m = len(map), len(map[0])
split = 0
for i in range(1, n) :
    for j in range(m) :
        if (map[i - 1][j] == '|' and map[i][j] == '.') :
            map[i][j] = '|'
    for j in range(m) :
        if (map[i - 1][j] == '|' and map[i][j] == '^') :
            split += 1
            if (j > 0 and map[i][j - 1] == '.') :
                map[i][j - 1] = '|'
            if (j < (m - 1) and map[i][j + 1] == '.') :
                map[i][j + 1] = '|'

print(split)