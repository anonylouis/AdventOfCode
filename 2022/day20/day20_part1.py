#!/usr/bin/python3

f = open('input.txt')

L = []
n = 0

for l in f :
	L.append([int(l[:-1]), n])
	n+=1

for i in range(n) :
	I = [e[1] for e in L]
	ind = I.index(i)
	if (L[ind][0] >= 0) :
		for j in range(L[ind][0]) :
			L[ind % n], L[(ind + 1) % n] = L[(ind + 1) % n], L[ind % n]
			ind += 1
	else :
		for j in range((-1) * L[ind][0]) :
			L[ind % n], L[(ind - 1) % n] = L[(ind - 1) % n], L[ind % n]
			ind -= 1

I = [e[0] for e in L]
zero = I.index(0)
groove = [L[(zero + 1000) % n][0], L[(zero + 2000) % n][0], L[(zero + 3000) % n][0]]
print(sum(groove))