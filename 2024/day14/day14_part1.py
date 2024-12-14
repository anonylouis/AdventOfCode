#!/usr/bin/python3
import re

f = open('input.txt')

size = [101, 103]
R = []

for line in f :
	line = re.search(r"p=([0-9]+),([0-9]+) v=([0-9\-]+),([0-9\-]+)", line)
	r = list(map(int, line.groups()))
	i = 100
	R.append([(r[0] + r[2] * i) % size[0], (r[1] + r[3] * i) % size[1]])

quarters = [0, 0, 0, 0]
for r in R :
	if r[0] < (size[0] // 2) and r[1] < (size[1] // 2) :
		quarters[0] += 1
	elif r[0] > (size[0] / 2) and r[1] < (size[1] // 2) :
		quarters[1] += 1
	elif r[0] < (size[0] // 2) and r[1] > (size[1] // 2) :
		quarters[2] += 1
	elif r[0] > (size[0] // 2) and r[1] > (size[1] // 2) :
		quarters[3] += 1

print(quarters[0] * quarters[1] * quarters[2] * quarters[3])