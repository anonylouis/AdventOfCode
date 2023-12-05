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
	for i in range(len(seeds)) :
		for ranges in category :
			if (ranges[2] < 1) :
				continue
			if ranges[1] <= seeds[i] < (ranges[1] + ranges[2]) :
				seeds[i] += ranges[0] - ranges[1]
				break

print(min(seeds))