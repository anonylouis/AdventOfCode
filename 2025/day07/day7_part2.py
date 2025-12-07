#!/usr/bin/python3

f = open('input.txt')
map = [list(line[:-1]) for line in f.readlines()]

n, m = len(map), len(map[0])
beams = { map[0].index('S') : 1 }

def add_to_dic(dic, key, value) :
    dic[key] = value if key not in dic else value + dic[key]

for i in range(1, n) :
    next_beams = {}
    for j in beams.keys() :
        if map[i][j] == '.' :
            add_to_dic(next_beams, j, beams[j])
        elif map[i][j] == '^' :
            if (j > 0 and map[i][j - 1] == '.') :
                add_to_dic(next_beams, j - 1, beams[j])
            if (j < (m - 1) and map[i][j + 1] == '.') :
                add_to_dic(next_beams, j + 1, beams[j])
    beams = next_beams

print(sum([beams[p] for p in beams]))
