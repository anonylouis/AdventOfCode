#!/usr/bin/python3
 
f = open('input.txt')

lists = []
for line in f :
	lists.append(list(map(int, line.split())))

c = 0
for l in lists :
	diff = [l[i] - l[i + 1] for i in range(len(l) - 1)]
	min_l , max_l = min(diff), max(diff)
	if (min_l * max_l > 0) :
		if (min_l < 0) :
			max_l, min_l = abs(min_l), abs(max_l)
		if (min_l >= 1 and max_l <= 3) :
			c += 1

print(c)
