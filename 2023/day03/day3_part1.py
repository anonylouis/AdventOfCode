#!/usr/bin/python3

f = open('input.txt')

lines = []
for line in f :
	lines.append(line[:-1])

i, s = 0, 0
while i < len(lines) :
	j = 0
	while j < len(lines[i]) :
		if (lines[i][j]).isdigit() :
			number = ""
			while (j < len(lines[i]) and (lines[i][j]).isdigit()) :
				number += lines[i][j]
				j+=1
			border = ""
			if (i != 0) :
				border += lines[i - 1][max(0, j - len(number) - 1) : min(len(lines[i - 1]), j + 1)]
			if (i != (len(lines) - 1)) :
				border += lines[i + 1][max(0, j - len(number) - 1) : min(len(lines[i + 1]), j + 1)]
			if (j - len(number) != 0) :
				border += lines[i][j - len(number) - 1]
			if (j < len(lines[i])) :
				border += lines[i][j]
			if (any([not k.isdigit() and k != '.' for k in border])) :
				s += int(number)
		else :
			j+=1
	i += 1
print(s)
