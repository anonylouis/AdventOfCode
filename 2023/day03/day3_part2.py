#!/usr/bin/python3

f = open('input.txt')

lines = []
for line in f :
	lines.append(line[:-1])

i, s = 0, 0
while i < len(lines) :
	j = 0
	while j < len(lines[i]) :
		if lines[i][j] == '*':
			N = []
			if (i != 0) :
				border = ""
				border_min, border_max = max(0, j - 1), min(len(lines[i - 1]) - 1, j + 1)
				if (border_min > 0 and lines[i - 1][border_min].isdigit()) :
					while(border_min > 0 and lines[i - 1][border_min - 1].isdigit()) :
						border_min -= 1
				if (border_max < (len(lines[i - 1]) - 1) and lines[i - 1][border_max].isdigit()) :
					while(border_max < (len(lines[i - 1]) - 1) and lines[i - 1][border_max + 1].isdigit()) :
						border_max += 1
				border += lines[i - 1][border_min : border_max + 1]
				border = ''.join([k if k.isdigit() else ' ' for k in border])
				N += list(map(int, border.split()))
			if (i != (len(lines) - 1)) :
				border = ""
				border_min, border_max = max(0, j - 1), min(len(lines[i + 1]) - 1, j + 1)
				if (border_min > 0 and lines[i + 1][border_min].isdigit()) :
					while(border_min > 0 and lines[i + 1][border_min - 1].isdigit()) :
						border_min -= 1
				if (border_max < (len(lines[i + 1]) - 1) and lines[i + 1][border_max].isdigit()) :
					while(border_max < (len(lines[i + 1]) - 1) and lines[i + 1][border_max + 1].isdigit()) :
						border_max += 1
				border += lines[i + 1][border_min : border_max + 1]
				border = ''.join([k if k.isdigit() else ' ' for k in border])
				N += list(map(int, border.split()))
			if (j != 0) :
				border = ""
				border_min = j - 1
				if (border_min > 0 and lines[i][border_min].isdigit()) :
					while(border_min > 0 and lines[i][border_min - 1].isdigit()) :
						border_min -= 1
				border += lines[i][border_min : j]
				border = ''.join([k if k.isdigit() else ' ' for k in border])
				N += list(map(int, border.split()))
			if (j < len(lines[i])) :
				border = ""
				border_max = j + 1
				if (border_max < len(lines[i]) and lines[i][border_max].isdigit()) :
					while(border_max < (len(lines[i]) - 1) and lines[i][border_max + 1].isdigit()) :
						border_max += 1
				border += lines[i][j + 1 : border_max + 1]
				border = ''.join([k if k.isdigit() else ' ' for k in border])
				N += list(map(int, border.split()))
			if (len(N) == 2) :
				s += N[0] * N[1]
		j+=1
	i += 1
print(s)
