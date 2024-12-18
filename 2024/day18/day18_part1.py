#!/usr/bin/python3

f = open('input.txt')
to_fall = []
for line in f :
	to_fall.append(list(map(int, line[:-1].split(','))))

size = 71
step = 1024

M = [[-1 for i in range(size)] for j in range(size)]

for byte in to_fall[:step] :
	M[byte[1]][byte[0]] = False

M[0][0] = 0
queue = [[0, 0]]
while len(queue) != 0 :
	i, j = queue.pop()
	if i > 0 and M[i - 1][j] != False :
		tmp = M[i - 1][j]
		if M[i - 1][j] == -1 : M[i - 1][j] = M[i][j] + 1
		else : M[i - 1][j] = min(M[i][j] + 1, M[i - 1][j])
		if tmp != M[i - 1][j] :
			queue.append([i - 1, j])
	if i < (size - 1) and M[i + 1][j] != False :
		tmp = M[i + 1][j]
		if M[i + 1][j] == -1 : M[i + 1][j] = M[i][j] + 1
		else : M[i + 1][j] = min(M[i][j] + 1, M[i + 1][j])
		if tmp != M[i + 1][j] :
			queue.append([i + 1, j])
	if j > 0 and M[i][j - 1] != False :
		tmp = M[i][j - 1]
		if M[i][j - 1] == -1 : M[i][j - 1] = M[i][j] + 1
		else : M[i][j - 1] = min(M[i][j] + 1, M[i][j - 1])
		if tmp != M[i][j - 1] :
			queue.append([i, j - 1])
	if j < (size - 1) and M[i][j + 1] != False :
		tmp = M[i][j + 1]
		if M[i][j + 1] == -1 : M[i][j + 1] = M[i][j] + 1
		else : M[i][j + 1] = min(M[i][j] + 1, M[i][j + 1])
		if tmp != M[i][j + 1] :
			queue.append([i, j + 1])

print(M[size - 1][size - 1])