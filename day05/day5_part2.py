#!/usr/bin/python3

f = open('input.txt')

L=[]
for l in f :
	if (l=="\n") :
		break
	L.append(l[:-1])

column_nb = len((L.pop()).split())

for i in range(len(L)) :
	L[i] = L[i]+ " "*(4 * column_nb - 1 -len(L[i]))
	tmp = list(L[i])
	for j in range(column_nb) :
		if (tmp[1+j*4] == " ") :
			tmp[1+j*4] = '0'
	L[i] = ''.join(tmp).replace('[', ' ').replace(']', ' ').split()

piles = []

for i in range(column_nb) :
	piles.append([])
	for j in range(len(L)-1, -1, -1) :
		if (L[j])[i] != "0" : 
			(piles[i]).append(((L[j])[i]))

for l in f :
	l = l[:-1].split()
	nb_to_move, pile_from, pile_to = int(l[1]), int(l[3]) - 1, int(l[5]) - 1
	for i in range(-1 * nb_to_move, 0) :
		(piles[pile_to]).append((piles[pile_from])[i])
	for i in range(nb_to_move) :
		piles[pile_from].pop()

print(''.join(piles[j][-1] for j in range(len(piles))))