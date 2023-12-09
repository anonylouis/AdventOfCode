#!/usr/bin/python3

from math import *

f = open('input.txt')

s = 0
for l in f :
	H = [list(map(int, l[:-1].split()))]
	while (any(H[-1])) :
		H.append([H[-1][i + 1] - H[-1][i] for i in range(len(H[-1]) - 1)])
	H[-1].append(0)
	while(len(H)  != 1) :
		H[-2].append(H[-2][-1] + H[-1][-1])
		H.pop()
	s += H[0][-1]
print(s)