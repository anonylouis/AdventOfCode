#!/usr/bin/python3

f = open('input.txt')

MAP=[]
S = []

i = 0
for l in f :
	if l.count('S') > 0 :
		S = [i, l.find('S')]
		l = l.replace('S', 'a')
	if l.count('E') > 0 :
		E = [i, l.find('E')]
		l = l.replace('E', 'z')
	MAP.append(l[:-1])
	i+=1

j = len(MAP[0])
E = E[0] * j + E[1]

D = [-1] * (i * j)
D[S[0] * j + S[1]] = 0
# -1 = inf distance
# -2 = eliminated

def find_min(p) :
	L= [[p[i], i] for i in range(len(p)) if p[i] >= 0]
	if len(L) > 0 :
		return (min(L)[1])
	return (-1)

# Disjkrat algorithm implementation
while sum(D) != (-2 * len(D)) :
	s = find_min(D)
	if s == E:
		break
	s_y = s // j
	s_x = s % j

	if s_y > 0 and (ord(MAP[s_y -1][s_x]) - ord(MAP[s_y][s_x])) <= 1 :
		if D[(s_y - 1) * j + s_x] > -1 :
			if D[(s_y - 1) * j + s_x] > (D[s] + 1) :
				D[(s_y - 1) * j + s_x] =  D[s] + 1
		elif D[(s_y - 1) * j + s_x] == -1:
			D[(s_y - 1) * j + s_x] = D[s] + 1

	if s_y < (i - 1) and (ord(MAP[s_y + 1][s_x]) - ord(MAP[s_y][s_x])) <= 1 :
		if D[(s_y + 1) * j + s_x] > -1 :
			if D[(s_y + 1) * j + s_x] > (D[s] + 1) :
				D[(s_y + 1) * j + s_x] =  D[s] + 1
		elif D[(s_y + 1) * j + s_x] == -1 :
			D[(s_y + 1) * j + s_x] = D[s] + 1

	if s_x > 0 and (ord(MAP[s_y][s_x - 1]) - ord(MAP[s_y][s_x])) <= 1 :
		if D[s_y * j + s_x - 1] > -1 :
			if D[s_y * j + s_x - 1] > (D[s] + 1) :
				D[s_y * j + s_x - 1] =  D[s] + 1
		elif D[s_y * j + s_x - 1] == -1:
			D[s_y * j + s_x - 1]= D[s] + 1

	if s_x < (j - 1) and (ord(MAP[s_y][s_x + 1]) - ord(MAP[s_y][s_x])) <= 1:
		if D[s_y * j + s_x + 1] > -1 :
			if D[s_y * j + s_x + 1] > (D[s] + 1) :
				D[s_y * j + s_x + 1] =  D[s] + 1
		elif D[s_y * j + s_x + 1] == -1:
			D[s_y * j + s_x + 1]= D[s] + 1
	
	D[s] = -2
print(D[E])