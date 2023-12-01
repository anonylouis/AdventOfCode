#!/usr/bin/python3

f = open('input.txt')

map = []

for l in f :
	map.append([int(i) for i in l[:-1]])

c = 0
for i in range(len(map)) :
	for j in range(len(map[0])) :
		if i == 0 or i == (len(map) - 1) or j == 0 or j == (len(map[0]) -1) :
			c+=1
		else :
			tmp = [0, 0, 0, 0]
			for k in range(i - 1, -1, -1) : #top
				if (map[k][j] >= map[i][j]) :
					tmp[0] = 1
					break
			for k in range(i + 1, len(map)) : #down
				if (map[k][j] >= map[i][j]) :
					tmp[1] = 1
					break
			for k in range(j - 1, -1, -1) : #left
				if (map[i][k] >= map[i][j]) :
					tmp[2] = 1
					break
			for k in range(j + 1, len(map[0])) : #right
				if (map[i][k] >= map[i][j]) :
					tmp[3] = 1
					break
			if sum(tmp) < 4 :
				c+=1

print(c)
