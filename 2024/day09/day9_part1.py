#!/usr/bin/python3
from collections import deque

line = open('input.txt').readline()

file_id = 0

##  disk array of [file_id, number]
disk = []
for i, letter in enumerate(line) :
	number = int(letter)
	if i % 2 == 0 :
		disk.append([file_id, number])
		file_id += 1
	elif number != 0 :
		disk.append([-1, number])
disk = deque(disk)

final_hash = 0
final_id = 0
## increase_hash returning [new hash, new final_id]
increase_hash = lambda v, n : [final_hash + v * (final_id * n + (n * (n - 1)) // 2), final_id + n]

while len(disk) :
	file_id, number = disk.popleft()
	if file_id >= 0 :
		final_hash, final_id = increase_hash(file_id, number)
	else :
		try :
			file_id2, number2 = disk.pop()
			if file_id2 >= 0 :
				if number2 >= number :
					final_hash, final_id = increase_hash(file_id2, number)
					if number2 != number :
						disk.append([file_id2, number2 - number])
				else :
					final_hash, final_id = increase_hash(file_id2, number2)
					disk.appendleft([-1, number - number2])
			else :
				disk.appendleft([file_id, number])
		except IndexError :
			break

print(final_hash)