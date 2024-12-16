#!/bin/python3
 
f = open('input.txt')
 
M, S, E = [], [], []
NORTH, SOUTH, WEST, EAST = range(4)

for line in f :
	if line.count('S') :
		S = [len(M), line.index('S'), 'E']
	if line.count('E') :
		E = [len(M), line.index('E')]
	M.append(list(line[:-1]))

def print_map(_M) :
	for line in _M :
		print(''.join(line))

print_map(M)
print(M[S[0]][S[1]], S)
print(M[E[0]][E[1]], E)

Graph = {}

def get_nb_path(_i, _j) :
	nb_path = 0
	if M[_i][_j + 1] == '.' :
		nb_path += 1
	elif M[_i][_j - 1] == '.' :
		nb_path += 1
	elif M[_i + 1][_j] == '.' :
		nb_path += 1
	elif M[_i - 1][_j] == '.' :
		nb_path += 1
	return nb_path

def get_next_inter(_i, _j, _dir) :
	previus = [_i, _j]
	if _dir == EAST :
		_i += 1
	elif _dir == WEST :
		_i -= 1
	elif _dir == NORTH :
		_j -= 1
	else : # SOUTH
		_j += 1
	if M[_i][_j] == '#' :
		return False
	while get_nb_path(_i, _j) == 2 :
		if M[_i][_j + 1] == '.' and (_j + 1) != previus[1] :
			previus  = [_i, _j]
			_j += 1
		elif M[_i][_j - 1] == '.' and (_j - 1) != previus[1] :
			previus  = [_i, _j]
			_j -= 1
		elif M[_i + 1][_j] == '.' and (_i + 1) != previus[0] :
			previus  = [_i, _j]
			_i += 1
		elif M[_i - 1][_j] == '.' and (_i - 1) != previus[0] :
			previus  = [_i, _j]
			_i -= 1
	return [_i, _j]

def get_dist(_A, _B) :
	return abs(_A[0] - _B[0]) + abs(_A[1] - _B[1])

## INIT GRAPH
inters = [S]
while len(inters) != 0 :
	current = inters.pop()
	current_paths = []
	tmp = get_next_inter(current[0], current[1], EAST)
	if tmp :
		current_paths.append([tmp[0], tmp[1], get_dist(current, tmp)])
	tmp = get_next_inter(current[0], current[1], WEST)
	if tmp :
		current_paths.append([tmp[0], tmp[1], get_dist(current, tmp)])
	tmp = get_next_inter(current[0], current[1], NORTH)
	if tmp :
		current_paths.append([tmp[0], tmp[1], get_dist(current, tmp)])
	tmp = get_next_inter(current[0], current[1], SOUTH)
	if tmp :
		current_paths.append([tmp[0], tmp[1], get_dist(current, tmp)])
	
	print(current_paths)
	break

