#!/usr/bin/python3

f = open('input.txt')
to_fall = []
for line in f :
	to_fall.append(list(map(int, line[:-1].split(','))))

size = 71
steps = [0, len(to_fall) - 1]

while True :
	M = [[-1 for i in range(size)] for j in range(size)]
	step = steps[0] + (steps[1] - steps[0]) // 2
	for byte in to_fall[:step] :
		M[byte[1]][byte[0]] = False
	M[0][0] = 0
	queue = [[0, 0]]
	while len(queue) != 0 :
		i, j = queue.pop()
		if i > 0 and M[i - 1][j] == -1 :
			M[i - 1][j] = 0
			queue.append([i - 1, j])
		if i < (size - 1) and M[i + 1][j] == -1 :
			M[i + 1][j] = 0
			queue.append([i + 1, j])
		if j > 0 and M[i][j - 1] == -1 :
			M[i][j - 1] = 0
			queue.append([i, j - 1])
		if j < (size - 1) and M[i][j + 1] == -1 :
			M[i][j + 1] = 0
			queue.append([i, j + 1])

	if M[size - 1][size - 1] == 0 :
		steps[0] = step + 1
	else :
		steps[1] = step - 1
	if (steps[1] - steps[0]) <= 1 :
		print(to_fall[steps[1]])
		break