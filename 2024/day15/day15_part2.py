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
		M.append(list(line[:-1].replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")))
		if M[-1].count('@') :
			x, y = M[-1].index('@'), len(M) - 1

for move in moves :
	if move == '<' :	
		i = x - 1
		while M[y][i] == '[' or M[y][i] == ']':	
			i -= 1
		if  M[y][i] == '.' :
			while i < x :
				M[y][i] = M[y][i + 1]
				i += 1
			M[y][x] = '.'
			x -= 1
	elif move == '>' :
		i = x + 1
		while M[y][i] == '[' or M[y][i] == ']':
			i += 1
		if  M[y][i] == '.' :
			while i > x :
				M[y][i] = M[y][i - 1]
				i -= 1
			M[y][x] = '.'
			x += 1
	elif move == '^' :
		d = {}
		d[y] = set([x])
		index = y
		while d and len(d[index]) :
			index -= 1
			d[index] = set()
			x_boxes = d[index + 1]
			for x_box in x_boxes :
				if M[index][x_box] == '[' :
					d[index].update([x_box, x_box + 1])
				elif M[index][x_box] == ']' :
					d[index].update([x_box - 1, x_box])
				elif M[index][x_box] == '#' :
					d = False
					break
		if d : #  can move
			index += 1
			while index <= y :
				x_boxes = d[index]
				for x_box in x_boxes :
					M[index - 1][x_box] = M[index][x_box]
				for x_box in x_boxes :
					M[index][x_box] = '.'
				index += 1
			y -= 1
	elif move == 'v' :
		d = {}
		d[y] = set([x])
		index = y
		while d and len(d[index]) :
			index += 1
			d[index] = set()
			x_boxes = d[index - 1]
			for x_box in x_boxes :
				if M[index][x_box] == '[' :
					d[index].update([x_box, x_box + 1])
				elif M[index][x_box] == ']' :
					d[index].update([x_box - 1, x_box])
				elif M[index][x_box] == '#' :
					d = False
					break
		if d : #  can move
			index -= 1
			while index >= y :
				x_boxes = d[index]
				for x_box in x_boxes :
					M[index + 1][x_box] = M[index][x_box]
				for x_box in x_boxes :
					M[index][x_box] = '.'
				index -= 1
			y += 1

sum_box_scores = 0
for i in range(1, len(M) -1) :
	for j in range(1, len(M[0]) - 1) :
		if M[i][j] == '[' :
			sum_box_scores += 100 * i + j

print(sum_box_scores)