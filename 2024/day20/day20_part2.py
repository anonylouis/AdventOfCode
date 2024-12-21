#!/usr/bin/python3
from copy import deepcopy

f = open('input.txt')
M, S, E, starts = [], [], [], []
LIMIT = 21


for line in f :
	if line.count('S') :
		S = [len(M), line.index('S')]
	if line.count('E') :
		E = [len(M), line.index('E')]
	M.append(list(line[:-1]))

size = [len(M), len(M[0])]

M[S[0]][S[1]] = '.'
M[E[0]][E[1]] = '.'

for i in range(1, size[0] - 1) :
	for j in range(1, size[1] - 1) :
		if M[i][j] == '.' :
			starts.append([i, j])

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

def getCheats(_wall) :
	_cheats = {}
	for i in range(LIMIT) :
		for j in range(LIMIT - i) :
			pos = [(_wall[0] + i, _wall[1] + j), (_wall[0] - i, _wall[1] + j), (_wall[0] + i, _wall[1] - j), (_wall[0] - i, _wall[1] - j)]
			for p in pos :
				y, x = p
				if y > 0 and y < size[0] and x > 0 and x < size[1] and M[y][x] != '#' :
					_cheats[(y, x)] = i + j
	return _cheats

n = 0
for start in starts :
	cheats = getCheats(start)
	for end in cheats.keys() :
		totalDist = M[start[0]][start[1]] + MToEnd[end[0]][end[1]] + cheats[end]
		if ((noCheat - totalDist) >= 100) :
			n += 1

print(n)
