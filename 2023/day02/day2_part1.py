#!/usr/bin/python3

MAX_R, MAX_G, MAX_B = 12, 13, 14

f = open('input.txt')

index, s = 0, 0
for game in f :
	index += 1
	subsets = game.split(":", 1)[1].replace(',', ' ').split(';')
	is_valid = True
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
		if (r > MAX_R or g > MAX_G or b > MAX_B) :
			is_valid = False
	if (is_valid) :
		s += index
print(s)