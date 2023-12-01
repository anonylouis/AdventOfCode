#!/usr/bin/python3

f = open('input.txt')

M = []
Elves = []

# if out of range increase X !!
X = 20

n = X
for l in f :
	l = X*"."+l[:-1]+X*"."
	M.append(list(l))
	for i in range(len(l)) :
		if (l[i] == "#") :
			Elves.append([-1, n, i])
	n += 1

for p in range(X) :
	M.insert(0, list("."*len(M[0])))
	M.append(list("."*len(M[0])))

def	turn(n) :
	coord = []
	proposed = []
	for e in Elves :
		around=M[e[1] - 1][e[2] - 1] + M[e[1]][e[2] - 1] + M[e[1] + 1][e[2] - 1] + M[e[1] - 1][e[2]] + M[e[1] + 1][e[2]] + M[e[1] - 1][e[2] + 1] + M[e[1]][e[2] + 1] + M[e[1] + 1][e[2] + 1]
		i = 4
		if around.count("#") > 0 :
			i = 0
			while i < 4 :
				e[0] = (n + i) % 4
				if e[0] == 0 :
					if M[e[1] - 1][e[2] - 1] == '.' and M[e[1] - 1][e[2]] == '.' and M[e[1] - 1][e[2] + 1] == '.' :
						coord.append([e[1],e[2]])
						proposed.append([e[1] - 1, e[2]])
						break
				elif e[0] == 1 :
					if M[e[1] + 1][e[2] - 1] == '.' and M[e[1] + 1][e[2]] == '.' and M[e[1] + 1][e[2] + 1] == '.' :
						coord.append([e[1],e[2]])
						proposed.append([e[1] + 1, e[2]])
						break
				elif e[0] == 2 :
					if M[e[1] - 1][e[2] - 1] == '.' and M[e[1]][e[2] - 1] == '.' and M[e[1] + 1][e[2] - 1] == '.' :
						coord.append([e[1],e[2]])
						proposed.append([e[1], e[2] - 1])
						break
				else :
					if  M[e[1] - 1][e[2] + 1] == '.' and M[e[1]][e[2] + 1] == '.' and M[e[1] + 1][e[2] + 1] == '.' :
						coord.append([e[1],e[2]])
						proposed.append([e[1], e[2] + 1])
						break
				i+=1
		if i == 4 :
			coord.append(0)
			proposed.append(0)
	nb_move = 0
	for i in range(len(coord)) :
		if coord[i] != 0 and proposed.count(proposed[i]) == 1 :
			M[proposed[i][0]][proposed[i][1]] = '#'
			M[coord[i][0]][coord[i][1]] = '.'
			Elves[i][1], Elves[i][2] = proposed[i][0], proposed[i][1]
			nb_move+=1
	return nb_move

nb_turn = 0
while  nb_turn < 10 :
	nb_move = turn(nb_turn)
	nb_turn+=1

Y = [e[1] for e in Elves]
min_y, max_y = min(Y), max(Y)

X = [e[2] for e in Elves]
min_x, max_x = min(X), max(X)

smaller_rect = "".join([M[k][l] for k in range(min_y, max_y + 1) for l in range(min_x, max_x + 1)])
print(smaller_rect.count('.'))
