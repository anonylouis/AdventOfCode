#!/usr/bin/python3
from copy import deepcopy

f = open('input.txt')
M, S, E, Walls = [], [], [], []
LIMIT = 20


for line in f :
	if line.count('S') :
		S = [len(M), line.index('S')]
	if line.count('E') :
		E = [len(M), line.index('E')]
	M.append(list(line[:-1]))

size = [len(M), len(M[0])]

for i in range(1, size[0] - 1) :
	for j in range(1, size[1] - 1) :
		if M[i][j] == '#' and (M[i - 1][j] == '.' or M[i + 1][j] == '.' or M[i][j - 1] == '.' or M[i][j + 1] == '.') :
			Walls.append([i, j])

M[S[0]][S[1]] = '.'
M[E[0]][E[1]] = '.'

def floodFill(_M, _queue) :
	while len(_queue) != 0 :
		i, j = _queue.pop()
		if i > 0 and _M[i - 1][j] != '#':
			tmp = _M[i - 1][j]
			if _M[i - 1][j] == '.' : _M[i - 1][j] = _M[i][j] + 1
			else : _M[i - 1][j] = min(_M[i][j] + 1, _M[i - 1][j])
			if tmp != _M[i - 1][j] :
				_queue.append([i - 1, j])
		if i < (size[0] - 1) and _M[i + 1][j] != '#':
			tmp = _M[i + 1][j]
			if _M[i + 1][j] == '.' : _M[i + 1][j] = _M[i][j] + 1
			else : _M[i + 1][j] = min(_M[i][j] + 1, _M[i + 1][j])
			if tmp != _M[i + 1][j] :
				_queue.append([i + 1, j])
		if j > 0 and _M[i][j - 1] != '#':
			tmp = _M[i][j - 1]
			if _M[i][j - 1] == '.' : _M[i][j - 1] = _M[i][j] + 1
			else : _M[i][j - 1] = min(_M[i][j] + 1, _M[i][j - 1])
			if tmp != _M[i][j - 1] :
				_queue.append([i, j - 1])
		if j < (size[1] - 1) and _M[i][j + 1] != '#':
			tmp = _M[i][j + 1]
			if _M[i][j + 1] == '.' : _M[i][j + 1] = _M[i][j] + 1
			else : _M[i][j + 1] = min(_M[i][j] + 1, _M[i][j + 1])
			if tmp != _M[i][j + 1] :
				_queue.append([i, j + 1])



MToEnd = deepcopy(M)
MToEnd[E[0]][E[1]] = 0
floodFill(MToEnd, [E])

M[S[0]][S[1]] = 0
floodFill(M, [S])

assert MToEnd[S[0]][S[1]] == M[E[0]][E[1]]
noCheat = M[E[0]][E[1]]

n = 0
for wall in Walls :
	wall_i, wall_j = wall
	bordersFromStart = [k for k in [M[wall_i - 1][wall_j], M[wall_i + 1][wall_j], M[wall_i][wall_j - 1], M[wall_i][wall_j + 1]] if k != '#']
	bordersToEnd = [k for k in [MToEnd[wall_i - 1][wall_j], MToEnd[wall_i + 1][wall_j], MToEnd[wall_i][wall_j - 1], MToEnd[wall_i][wall_j + 1]] if k != '#']

	totalDist = min(bordersFromStart) + min(bordersToEnd) + 1
	if ((noCheat - totalDist) >= 100) :
		n += 1

print(n)