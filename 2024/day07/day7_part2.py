#!/usr/bin/python3

f = open('input.txt')

R = []

for line in f :
	line = line[:-1].split(":")
	result = int(line[0])
	R.append([result, list(map(int,line[1].split()))])

total = 0

for r in R :
	result, numbers = r
	PATH = set()
	for n in numbers :
		if len(PATH) == 0:
			PATH.add(n)
		else :
			to_add = []
			for p in PATH :
				to_add.append(p + n)
				to_add.append(p * n)
				to_add.append(int(str(p) + str(n)))
			PATH = set(to_add)
	if result in PATH :
		total += result

print(total)
