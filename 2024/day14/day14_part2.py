#!/usr/bin/python3
import re

f = open('input.txt')
output = open('output.txt', 'w')

size = [101, 103]
R = []

for line in f :
	line = re.search(r"p=([0-9]+),([0-9]+) v=([0-9\-]+),([0-9\-]+)", line)
	R.append(list(map(int, line.groups())))
for i in [13 + 101 * k for k in range(100)] :
	M = [['.' for i in range(size[0])] for j in range(size[1])]
	for r in R :
		x, y = (r[0] + r[2] * i) % size[0], (r[1] + r[3] * i) % size[1]
		M[y][x] = 'p'
	output.write("after " + str(i) + " seconds : \n")
	for line in M :
		output.write(''.join(line) + "\n")

