#!/usr/bin/python3

f = open('input.txt')
map = []

for line in f :
    map.append(line[:-1])

n, m = len(map), len(map[0])
s = 0
for i in range(n) :
    for j in range(m) :
        if map[i][j] == '@' :
            border = ""
            if (i > 0) :
                if (j > 0) :
                    border += map[i - 1][j - 1]
                border += map[i - 1][j]
                if (j < (m - 1)) :
                    border += map[i - 1][j + 1]

            if (j > 0) :
                border += map[i][j - 1]
            if (j < (m - 1)) :
                border += map[i][j + 1]
            
            if (i < (n - 1)) :
                if (j > 0) :
                    border += map[i + 1][j - 1]
                border += map[i + 1][j]
                if (j < (m - 1)) :
                    border += map[i + 1][j + 1]

            if (border.count('@') < 4) :
                s += 1

print(s)