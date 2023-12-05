#!/usr/bin/python3

f = open('input.txt')

lines = []
seeds = list(map(int, f.readline().split(':', 1)[1].split()))
f.readline()

maps = []
current = []
for line in f :
	if (line.find(':') != -1) :
		continue
	if (line == "\n") :
		maps.append(current.copy())
		current = []
		continue
	current.append(list(map(int, line[:-1].split())))
if (current != []) :
	maps.append(current)

for category in maps :
	tmp = []
	i = 0
	while (i < len(seeds)) :
		seed_min = seeds[i]
		seed_max = seed_min + seeds[i + 1] - 1
		i += 2
		found_range = False
		for ranges in category :
			if (ranges[2] < 1) :
				continue
			if ranges[1] <= seed_min < (ranges[1] + ranges[2]) :
				found_range = True
				delta = ranges[0] - ranges[1]
				tmp.append(seed_min + delta)
				if (seed_max < (ranges[1] + ranges[2])) :
					tmp.append(seed_max - seed_min + 1)
				else :
					tmp.append((ranges[1] + ranges[2] - 1) - seed_min + 1)
					seeds.append(ranges[1] + ranges[2])
					seeds.append(seed_max - ranges[1] - ranges[2] + 1)
				break
		if (not found_range) :
			tmp.append(seed_min)
			tmp.append(seed_max - seed_min + 1)
	seeds = tmp.copy()

print(min(seeds[::2]))
