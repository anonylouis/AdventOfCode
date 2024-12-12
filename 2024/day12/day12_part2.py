#!/usr/bin/python3
 
f = open('input.txt')

M = []

for line in f :
	M.append(list(line[:-1]))

n, m = len(M), len(M[0])
price = 0 

def addValueToMap(_map, _key, _value, _dir) :
	if _key not in _map :
		_map[_key] = set()
	_map[_key].add((_value, _dir))

def getFaceNumber(_map) :
	faces = 0
	for _key in _map :
		fences = sorted(list(_map[_key]))
		pads = [True]
		if len(fences) > 1 :
			# fences are 2+ blocks far away, or they have two differents directions 
			pads += [(fences[i + 1][0] - fences[i][0]) > 1 or fences[i + 1][1] != fences[i][1] for i in range(len(fences) - 1)]
		faces += sum(pads)
	return faces


for i in range(n) :
	for j in range(m) :
		plant = M[i][j]
		if type(plant) != int :
			already_visited = ord(plant)
			plant_number = 0
			vertical_fences = {}
			horizontal_fences = {}
			region = set()
			region.add((i,j))
			while len(region) :
				current_i, current_j = region.pop()
				if current_i > 0 and M[current_i - 1][current_j] == plant :
					region.add((current_i - 1, current_j))
				elif current_i == 0 or M[current_i - 1][current_j] != already_visited :
					addValueToMap(horizontal_fences, current_i, current_j, -1)
				if current_i < (n - 1) and M[current_i + 1][current_j] == plant :
					region.add((current_i + 1, current_j))
				elif current_i == (n - 1) or M[current_i + 1][current_j] != already_visited :
					addValueToMap(horizontal_fences, current_i + 1, current_j, 1)
				if current_j > 0 and M[current_i][current_j - 1] == plant :
					region.add((current_i, current_j - 1))
				elif current_j == 0 or M[current_i][current_j - 1] != already_visited :
					addValueToMap(vertical_fences, current_j, current_i, -1)
				if current_j < (m - 1) and M[current_i][current_j + 1] == plant :
					region.add((current_i, current_j + 1))
				elif current_j == (m - 1) or M[current_i][current_j + 1] != already_visited :
					addValueToMap(vertical_fences, current_j + 1, current_i, 1)
				plant_number += 1
				M[current_i][current_j] = already_visited
			price += plant_number * (getFaceNumber(horizontal_fences) + getFaceNumber(vertical_fences))

print(price)