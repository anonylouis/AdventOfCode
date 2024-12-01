#!/usr/bin/python3
import numpy as np

f = open('input.txt')

left = []
right = []
for line in f :
	a, b = map(int, line.split())
	left.append(a)
	right.append(b)

left.sort()
right.sort()

print(sum(map(abs, np.subtract(left, right))))