#!/usr/bin/python3

f = open('input.txt')

L = []
n = 0

for l in f :
	L.append([int(l[:-1]), n])
	n+=1

cpy = [[e[0], e[1]] for e in L]
for e in L :
	e[0] = (811589153 * e[0])

for nb in range(10) :
	print(nb)
	for i in range(n) :
		I = [e[1] for e in L]
		ind = I.index(i)
		if (L[ind][0] >= 0) :
			for j in range((L[ind][0]) % (n-1)) :
				L[ind % n], L[(ind + 1) % n] = L[(ind + 1) % n], L[ind % n]
				ind += 1
		else :
			for j in range(((-1) * L[ind][0]) % (n-1)) :
				L[ind % n], L[(ind - 1) % n] = L[(ind - 1) % n], L[ind % n]
				ind -= 1

I = [e[0] for e in L]
zero = I.index(0)
groove = [cpy[L[(zero + 1000) % n][1]][0], cpy[L[(zero + 2000) % n][1]][0], cpy[L[(zero + 3000) % n][1]][0]]
print(sum(groove) * 811589153)
