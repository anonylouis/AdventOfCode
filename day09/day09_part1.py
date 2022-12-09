#!/usr/bin/python3

f = open('input.txt')

head = [0, 0]
tail = [0, 0]
P = {(0, 0)}
for l in f :
	l = l[:-1].split()
	if l[0] == "L" :
		for c in range(int(l[1])) :
			head[0] -= 1
			if tail[0] > (head[0] + 1) :
				tail[0] -= 1
				tail[1] = head[1]
			P.add((tail[0], tail[1]))
	elif l[0] == "R" :
		for c in range(int(l[1])) :
			head[0] += 1
			if tail[0] < (head[0] - 1) :
				tail[0] += 1
				tail[1] = head[1]
			P.add((tail[0], tail[1]))
	elif l[0] == "D" :
		for c in range(int(l[1])) :
			head[1] -= 1
			if tail[1] > (head[1] + 1) :
				tail[0] = head[0]
				tail[1] -=1
			P.add((tail[0], tail[1]))
	elif l[0] == "U" :
		for c in range(int(l[1])) :
			head[1] += 1
			if tail[1] < (head[1] - 1) :
				tail[0] = head[0]
				tail[1] +=1
			P.add((tail[0], tail[1]))

print(len(P))