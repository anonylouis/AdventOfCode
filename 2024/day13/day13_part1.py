#!/usr/bin/python3
import re

f = open('input.txt')

A, B = [], []
token = 0

for line in f :
	if line.startswith("Button A") :
		A = list(map(int, re.sub(r"[a-zA-Z+,:]", "", line[:-1]).split()))
	elif line.startswith("Button B") :
		B = list(map(int, re.sub(r"[a-zA-Z+,:]", "", line[:-1]).split()))
	elif line.startswith("Prize") :
		Prize = list(map(int, re.sub(r"[a-zA-Z=,:]", "", line[:-1]).split()))
		x = (B[1] * Prize[0] - B[0] * Prize[1]) / (B[1] * A[0] - B[0] * A[1])
		y = (A[1] * Prize[0] - A[0] * Prize[1]) / (A[1] * B[0] - A[0] * B[1])
		if x == int(x) and y == int(y) :
			token += 3 * int(x) + int(y)

print(token)