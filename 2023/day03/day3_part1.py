#!/usr/bin/python3

f = open('input.txt')

lines = []
for line in f :
	lines.append(line)

i = 0
while i < range(len(lines)) :
	j = 0
	while j < range(len(lines[i])) :
		if (lines[i][j]).isdigit() :
			number = ""
			while(lines[i][j]).isdigit()) :
				number += lines[i][j]
				j+=1
			
		else :
			j+=1