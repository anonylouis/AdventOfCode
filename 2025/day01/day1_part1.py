#!/usr/bin/python3

f = open('input.txt')

s = 0
n = 50
M = 100

for line in f :
	distance = int(line[1:-1]) if line[0] == "R" else -int(line[1:-1])
	n = (n + distance) % M
	if (n < 0) :
		n += M
	if (n == 0) :
		s += 1

print(s)
