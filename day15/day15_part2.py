#!/usr/bin/python3
MIN=0
MAX=4000000

for y_search in range(MIN, MAX+1) :
	P  = []
	f = open('input.txt')
	for l in f :
		L=l[:-1].replace("=", " ").replace(",", " ").replace(":", " ").split()
		L = list(map(int, [L[3], L[5], L[11], L[13]]))
		d = abs(L[0] - L[2]) + abs(L[1] - L[3]) #distance
		pmin = -d + abs(L[1] - y_search)
		pmax =  d - abs(L[1] - y_search)
		if pmin <= pmax :
			pmin = L[0] + pmin
			pmax = L[0] + pmax
			if pmax >= MIN and pmin <= MAX :
				if pmin < MIN :
					pmin = MIN
				if pmax > MAX :
					pmax = MAX
				P.append([pmin, pmax])

	if len(P) != 0 :
		P.sort(key=lambda x : x[0])
		current_xmin = P[0][0]
		while len(P) != 0 :
			current_elem = P[0]
			current_xmin = current_elem[1] + 1
			while len(P) != 0 :
				e = P[0]
				if e[1] < current_xmin :
					P.remove(e)
				else :
					break
			if len(P) > 0 and P[0][0] > current_xmin :
				print(current_xmin, y_search)
				exit()


