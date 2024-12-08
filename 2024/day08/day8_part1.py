#!/usr/bin/python3

f = open('input.txt')

freqs = {}
pattern = r'[A-Za-z0-9]{1}'
width, height = 0, 0

for i, line in enumerate(f) :
	height = i
	width = len(line) - 1
	for j in range(len(line)) :
		letter = line[j]
		if letter.isalnum() :
			if letter in freqs :
				freqs[letter].append([i, j])
			else :
				freqs[letter] = [[i, j]]

antinodes = set()

for freq in freqs :
	positions = freqs[freq]
	for i in range(len(positions)) :
		for j in range(len(positions)) :
			if i != j :
				antenna1, antenna2 = positions[i], positions[j]
				if antenna1[0] > antenna2[0] :
					antenna1, antenna2 = antenna2, antenna1
				
				diffy, diffx = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]
				y1, x1 = antenna1[0] + diffy, antenna1[1] + diffx
				y2, x2 = antenna2[0] - diffy, antenna2[1] - diffx
				if (y1 >= 0 and y1 <= height and x1 >= 0 and x1 <= width) :
					antinodes.add((y1, x1))
				if (y2 >= 0 and y2 <= height and x2 >= 0 and x2 <= width) :
					antinodes.add((y2, x2))

print(len(antinodes))
