#!/usr/bin/python3

from math import *

f = open('input.txt')
T = list(map(int, f.readline()[:-1].split(":", 1)[1].split()))
D = list(map(int, f.readline()[:-1].split(":", 1)[1].split()))
n = len(T)

total = 1
for i in range(n) :
	delta = T[i] * T[i] - 4 * D[i]
	count = 1
	if (delta >= 0) :
		x1 = (T[i] - delta**0.5) / 2
		x2 = (T[i] + delta**0.5) / 2
		if x1 == ceil(x1) :
			x1 += 1
		if x2 == floor(x2) :
			x2 -= 1
		if (x2 >= x1) :
			count = floor(x2) - ceil(x1) + 1
	total *= count

print(total)