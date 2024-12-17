#!/bin/python3
 
f = open('input.txt')
 
M, S, E = [], [], []
NORTH, SOUTH, WEST, EAST = range(4)

for line in f :
	if line.count('S') :
		S = [len(M), line.index('S')]
	if line.count('E') :
		E = [len(M), line.index('E')]
	M.append(list(line[:-1]))

# N, S, W, E
to_explore = [S]
M[S[0]][S[1]] = [1000, 1000, 2 * 1000, 0]
M[E[0]][E[1]] = '.'
while len(to_explore) != 0 :
	i, j = to_explore.pop()
	current_w = M[i][j]
	if M[i - 1][j] != '#' : # NORTH
		to_append = False
		current_w_min = min([current_w[0], current_w[1] + 2 * 1000, current_w[2] + 1000, current_w[3] + 1000])
		tmp = [current_w_min + 1, current_w_min + 1 + 2 * 1000, current_w_min + 1 + 1000, current_w_min + 1 + 1000]
		if M[i - 1][j] == '.' :
			M[i - 1][j] = tmp
			to_append = True
		else :
			to_append = tmp[0] < M[i - 1][j][0] or tmp[1] < M[i - 1][j][1] or tmp[2] < M[i - 1][j][2] or tmp[3] < M[i - 1][j][3]
			M[i - 1][j][0] = min(M[i - 1][j][0], tmp[0])
			M[i - 1][j][1] = min(M[i - 1][j][1], tmp[1])
			M[i - 1][j][2] = min(M[i - 1][j][2], tmp[2])
			M[i - 1][j][3] = min(M[i - 1][j][3], tmp[3])
		if to_append :
			to_explore.append([i - 1, j])
	if M[i + 1][j] != '#' : # SOUTH
		to_append = False
		current_w_min = min([current_w[0] + 2 * 1000, current_w[1], current_w[2] + 1000, current_w[3] + 1000])
		tmp = [current_w_min + 1 + 2 * 1000, current_w_min + 1, current_w_min + 1 + 1000, current_w_min + 1 + 1000]
		if M[i + 1][j] == '.' :
			M[i + 1][j] = tmp
			to_append = True
		else :
			to_append = tmp[0] < M[i + 1][j][0] or tmp[1] < M[i + 1][j][1] or tmp[2] < M[i + 1][j][2] or tmp[3] < M[i + 1][j][3]
			M[i + 1][j][0] = min(M[i + 1][j][0], tmp[0])
			M[i + 1][j][1] = min(M[i + 1][j][1], tmp[1])
			M[i + 1][j][2] = min(M[i + 1][j][2], tmp[2])
			M[i + 1][j][3] = min(M[i + 1][j][3], tmp[3])
		if to_append :
			to_explore.append([i + 1, j])
	if M[i][j - 1] != '#' : # WEST
		to_append = False
		current_w_min = min([current_w[0] + 1000, current_w[1] + 1000, current_w[2], current_w[3] + 1000])
		tmp = [current_w_min + 1 + 1000, current_w_min + 1 + 1000, current_w_min + 1, current_w_min + 1 + 1000]
		if M[i][j - 1] == '.' :
			M[i][j - 1] = tmp
			to_append = True
		else :
			to_append = tmp[0] < M[i][j - 1][0] or tmp[1] < M[i][j - 1][1] or tmp[2] < M[i][j - 1][2] or tmp[3] < M[i][j - 1][3]
			M[i][j - 1][0] = min(M[i][j - 1][0], tmp[0])
			M[i][j - 1][1] = min(M[i][j - 1][1], tmp[1])
			M[i][j - 1][2] = min(M[i][j - 1][2], tmp[2])
			M[i][j - 1][3] = min(M[i][j - 1][3], tmp[3])
		if to_append :
			to_explore.append([i, j - 1])
	if M[i][j + 1] != '#' : # EAST
		to_append = False
		current_w_min = min([current_w[0] + 1000, current_w[1] + 1000, current_w[2] + 2 * 1000, current_w[3]])
		tmp = [current_w_min + 1 + 1000, current_w_min + 1 + 1000, current_w_min + 1 + 2 * 1000, current_w_min + 1]
		if M[i][j + 1] == '.' :
			M[i][j + 1] = tmp
			to_append = True
		else :
			to_append = tmp[0] < M[i][j + 1][0] or tmp[1] < M[i][j + 1][1] or tmp[2] < M[i][j + 1][2] or tmp[3] < M[i][j + 1][3]
			M[i][j + 1][0] = min(M[i][j + 1][0], tmp[0])
			M[i][j + 1][1] = min(M[i][j + 1][1], tmp[1])
			M[i][j + 1][2] = min(M[i][j + 1][2], tmp[2])
			M[i][j + 1][3] = min(M[i][j + 1][3], tmp[3])
		if to_append :
			to_explore.append([i, j + 1])

best_path = min(M[E[0]][E[1]])

already_visited = set()
paths = [[E[0], E[1], best_path]]
while len(paths) != 0 :
	i, j, score = paths.pop()
	if (i, j, score) in already_visited :
		continue
	already_visited.add((i, j, score))
	if i == S[0] and j == S[1] :
		continue
	for dir in range(4) :
		if M[i][j][dir] == score :
			if M[i - 1][j] != '#' : # NORTH
				if dir == 0 :
					tmp = [score - 1 - 4 * 1000, score - 1 - 2 * 1000, score - 1 - 3 *1000 , score - 1 - 3 * 1000]
				elif dir == 1 :
					tmp = [score - 1 - 2 * 1000, score - 1, score - 1 - 1000 , score - 1 - 1000]
				elif dir == 2 :
					tmp = [score - 1 - 3 * 1000, score - 1 - 1000, score - 1 - 2 * 1000 , score - 1 - 2 * 1000]
				elif dir == 3 :
					tmp = [score - 1 - 3 * 1000, score - 1 - 1000, score - 1 - 2 * 1000 , score - 1 - 2 * 1000]
				for k in range(4) :
					if tmp[k] == M[i - 1][j][k] :
						paths.append([i - 1, j, tmp[k]])
			if M[i + 1][j] != '#' : # SOUTH
				if dir == 0 :
					tmp = [score - 1, score - 1 - 2 * 1000, score - 1 - 1000 , score - 1 - 1000]
				elif dir == 1 :
					tmp = [score - 1 - 2 * 1000, score - 1 - 4 * 1000, score - 1 - 3 * 1000 , score - 1 - 3 * 1000]
				elif dir == 2 :
					tmp = [score - 1 - 1000, score - 1 - 3 * 1000, score - 1 - 2 * 1000 , score - 1 - 2 * 1000]
				elif dir == 3 :
					tmp = [score - 1 - 1000, score - 1 - 3 * 1000, score - 1 - 2 * 1000 , score - 1 - 2 * 1000]
				for k in range(4) :
					if tmp[k] == M[i + 1][j][k] :
						paths.append([i + 1, j, tmp[k]])
			if M[i][j - 1] != '#' : # WEST
				if dir == 0 :
					tmp = [score - 1 - 2 * 1000, score - 1 - 2 * 1000, score - 1 - 3 * 1000 , score - 1 - 1000]
				elif dir == 1 :
					tmp = [score - 1 - 2 * 1000, score - 1 - 2 * 1000, score - 1 - 3 * 1000 , score - 1 - 1000]
				elif dir == 2 :
					tmp = [score - 1 - 3 * 1000, score - 1 - 3 * 1000, score - 1 - 4 * 1000 , score - 1 - 2 * 1000]
				elif dir == 3 :
					tmp = [score - 1 - 1000, score - 1 - 1000, score - 1 - 2 * 1000 , score - 1]
				for k in range(4) :
					if tmp[k] == M[i][j - 1][k] :
						paths.append([i, j - 1, tmp[k]])
			if M[i][j + 1] != '#' : # EAST
				if dir == 0 :
					tmp = [score - 1 - 2 * 1000, score - 1 - 2 * 1000, score - 1 - 1000 , score - 1 - 3 * 1000]
				elif dir == 1 :
					tmp = [score - 1 - 2 * 1000, score - 1 - 2 * 1000, score - 1 - 1000 , score - 1 - 3 * 1000]
				elif dir == 2 :
					tmp = [score - 1 - 1000, score - 1 - 1000, score - 1 , score - 1 - 2 * 1000]
				elif dir == 3 :
					tmp = [score - 1 - 3 * 1000, score - 1 - 3 * 1000, score - 1 - 2 * 1000 , score - 1 - 4 * 1000]
				for k in range(4) :
					if tmp[k] == M[i][j + 1][k] :
						paths.append([i, j + 1, tmp[k]])

print(len(set([(e[0], e[1]) for e in already_visited])))
