#!/usr/bin/python3

f = open('input.txt')

s = 0
n = 50
M = 100

for line in f :
	distance = int(line[1:-1])
	s += distance // M
	distance %= M

	if (distance == 0) :
		continue

	if line[0] == "L" :
		end = n - distance
		s += 1 if (n != 0) and (end < 0) or (end == 0) else 0
		if (end < 0) :
			end += M
	else :
		end = n + distance
		if (end >= M) :
			end -= M
			s += 1

	n = end % M

print(s)
