#!/usr/bin/python3

f = open('input.txt')

left = []
right = []
for line in f :
	a, b = map(int, line.split())
	left.append(a)
	right.append(b)



print(sum([i * right.count(i) for i in left]))