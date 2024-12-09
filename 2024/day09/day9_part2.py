#!/usr/bin/python3
from collections import deque

line = open('input.txt').readline()

file_id = 0

##  disk array of [file_id, number, moved]
disk = []
for i, letter in enumerate(line) :
	number = int(letter)
	if i % 2 == 0 :
		disk.append([file_id, number, False])
		file_id += 1
	elif number != 0 :
		disk.append([-1, number, False])


i = len(disk) - 1
while i >= 0 :
	file_id, number, moved = disk[i]
	if file_id >= 0 and not moved :
		for j in range(0, i) :
			if disk[j][0] == -1 and disk[j][1] >= number :
				space_number = disk[j][1]
				disk[j] = [file_id, number, True]
				disk[i] = [-1, number, False]
				if space_number > number :
					disk.insert(j + 1, [-1, space_number - number, False])
					i += 1
				break
	i -= 1

final_hash = 0
final_id = 0
## increase_hash returning [new hash, new final_id]
increase_hash = lambda v, n : [final_hash + v * (final_id * n + (n * (n - 1)) // 2), final_id + n]

for file in disk :
	file_id, number, moved = file
	if file_id >= 0 :
		final_hash, final_id = increase_hash(file_id, number)
	else :
		final_id += number

print(final_hash)