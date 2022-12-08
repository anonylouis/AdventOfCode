#!/usr/bin/python3

f = open('input.txt')

map = []

for l in f :
	map.append([int(i) for i in l[:-1]])

scenic = []
for i in range(len(map)) :
	for j in range(len(map[0])) :
		tmp = [0, 0, 0, 0]
		for k in range(i - 1, -1, -1) : #top
			tmp[0]+=1
			if (map[k][j] >= map[i][j]) :
				break
		for k in range(i + 1, len(map)) : #down
			tmp[1] += 1
			if (map[k][j] >= map[i][j]) :
				break
		for k in range(j - 1, -1, -1) : #left
			tmp[2] += 1
			if (map[i][k] >= map[i][j]) :
				break
		for k in range(j + 1, len(map[0])) : #right
			tmp[3] += 1
			if (map[i][k] >= map[i][j]) :
				break
		scenic.append(tmp[0] * tmp[1] * tmp[2] * tmp[3])

print(max(scenic))
