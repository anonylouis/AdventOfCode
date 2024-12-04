#!/usr/bin/python3

f = open('input.txt')

lines = []

for line in f :
	lines.append(line[:-1])

c = 0
n_lines = len(lines)
len_line = len(lines[0])

for i in range(1, n_lines - 1) :
	for j in range(1, len_line - 1) :
		if lines[i][j] == "A" :
			if (lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S") or (lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M") :
				if (lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S") or (lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M") :
					c += 1
print(c)