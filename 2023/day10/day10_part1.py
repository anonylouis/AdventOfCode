#!/usr/bin/python3

from math import *

f = open('input.txt')

def print_map(_M) :
	for l in M :
		print(''.join(map(str, l)))

M = []

for l in f :
	if ('S' in l) :
		S = [len(M), l.index('S')]
	M.append(list(l[:-1]))

M[S[0]][S[1]] = 0
L = [S]
n = 0
while(1) :
	if not len(L) :
		break
	tmp = []
	n += 1
	while len(L):
		i, j = L.pop()
		if (i != 0 and type(M[i - 1][j]) == str and  M[i - 1][j] in "|F7") :
			M[i - 1][j] = n
			tmp.append([i - 1, j])
		if (i != (len(M) - 1) and type(M[i + 1][j]) == str and M[i + 1][j] in "|LJ") :
			M[i + 1][j] = n
			tmp.append([i + 1, j])
		if  (j != 0 and type(M[i][j - 1]) == str and M[i][j - 1] in "-FL") :
			M[i][j - 1] = n
			tmp.append([i, j - 1])
		if  (j != (len(M[i]) - 1) and type(M[i][j + 1]) == str and M[i][j + 1] in "-J7") :
			M[i][j + 1] = n
			tmp.append([i, j + 1])
		
	L = tmp.copy()

print(n - 1)