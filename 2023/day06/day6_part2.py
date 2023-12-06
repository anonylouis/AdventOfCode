#!/usr/bin/python3

from math import *

f = open('input.txt')
T = int(f.readline()[:-1].split(":", 1)[1].replace(' ', ''))
D = int(f.readline()[:-1].split(":", 1)[1].replace(' ', ''))

delta = T * T - 4 * D
count = 0
if (delta >= 0) :
	x1 = (T - delta**0.5) / 2
	x2 = (T + delta**0.5) / 2
	if x1 == ceil(x1) :
		x1 += 1
	if x2 == floor(x2) :
		x2 -= 1
	if (x2 >= x1) :
		count = floor(x2) - ceil(x1) + 1

print(count)