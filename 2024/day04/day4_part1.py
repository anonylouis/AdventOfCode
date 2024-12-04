#!/usr/bin/python3

f = open('input.txt')

lines = []

for line in f :
	lines.append(line[:-1])

c = 0
n_lines = len(lines)
len_line = len(lines[0])

for i in range(n_lines) :
	for j in range(len(lines[0])) :
		if lines[i][j] == "X" :
			if (lines[i][j: j + 4] == "XMAS") :
				c += 1
			if (j >= 3 and lines[i][j - 3 : j + 1] == "SAMX") :
				c += 1
			if ((i + 4) <= n_lines) :
				v, d1, d2 = "", "", ""
				for k in range(i, i + 4) :
					v += lines[k][j]
					if (j - (k - i)) >= 0 :
						d1 += lines[k][j - (k - i)]
					if (j + (k - i)) < len_line :
						d2 += lines[k][j + (k - i)]
				if (v == "XMAS") :
					c += 1
				if (d1 == "XMAS") :
					c += 1
				if (d2 == "XMAS") :
					c += 1
			if (i >= 3) :
				v, d1, d2 = "", "", ""
				for k in range(i, i - 4, -1) :
					v += lines[k][j]
					if (j - (i - k)) >= 0 :
						d1 += lines[k][j - (i - k)]
					if (j + (i - k)) < len_line :
						d2 += lines[k][j + (i - k)]
				if (v == "XMAS") :
					c += 1
				if (d1 == "XMAS") :
					c += 1
				if (d2 == "XMAS") :
					c += 1
	
print(c)