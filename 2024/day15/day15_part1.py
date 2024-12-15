#!/usr/bin/python3

f = open('input.txt')

M = []
moves = ""
read_moves = False
x, y = 0, 0

for line in f :
	if line == "\n" :
		read_moves = True
	elif read_moves :
		moves += line[:-1]
	else :
		if line.count('@') :
			x, y = line.index('@'), len(M)
		M.append(list(line[:-1]))

for move in moves :
	if move == '<' :
		i = x - 1
		while M[y][i] == 'O' :
			i -= 1
		if  M[y][i] == '.' :
			while i < x :
				M[y][i] = M[y][i + 1]
				i += 1
			M[y][x] = '.'
			x -= 1
	elif move == '>' :
		i = x + 1
		while M[y][i] == 'O' :
			i += 1
		if  M[y][i] == '.' :
			while i > x :
				M[y][i] = M[y][i - 1]
				i -= 1
			M[y][x] = '.'
			x += 1
	elif move == '^' :
		i = y - 1
		while M[i][x] == 'O' :
			i -= 1
		if  M[i][x] == '.' :
			while i < y :
				M[i][x] = M[i + 1][x]
				i += 1
			M[y][x] = '.'
			y -= 1
	elif move == 'v' :
		i = y + 1
		while M[i][x] == 'O' :
			i += 1
		if  M[i][x] == '.' :
			while i > y :
				M[i][x] = M[i - 1][x]
				i -= 1
			M[y][x] = '.'
			y += 1

sum_box_scores = 0
for i in range(1, len(M) -1) :
	for j in range(1, len(M[0]) - 1) :
		if M[i][j] == 'O' :
			sum_box_scores += 100 * i + j

print(sum_box_scores)