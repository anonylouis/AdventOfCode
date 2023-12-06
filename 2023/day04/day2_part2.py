#!/usr/bin/python3

f = open('input.txt')

s = 0
for game in f :
	subsets = game.split(":", 1)[1].replace(',', ' ').split(';')
	M = [0, 0, 0]
	for subset in subsets :
		subset = subset.split()
		r,g,b = 0, 0, 0
		for i in range(0, len(subset), 2) :
			if (subset[i + 1] == "red") :
				r += int(subset[i])
			elif (subset[i + 1] == "green") :
				g += int(subset[i])
			else :
				b += int(subset[i])
		M[0], M[1], M[2] = max(M[0], r), max(M[1], g), max(M[2], b)
	s += M[0] * M[1] * M[2]
print(s)