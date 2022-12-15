#!/usr/bin/python3

f = open('input.txt')

BS = []
P  = []
y_search = 2000000

for l in f :
	L=l[:-1].replace("=", " ").replace(",", " ").replace(":", " ").split()
	L = list(map(int, [L[3], L[5], L[11], L[13]]))
	if (L[1] == y_search and L[0] not in BS) :
		#print("on ajoute le signal ", l)
		BS.append(L[0])
	if (L[3] == y_search and L[2] not in BS) :
		#print("on ajoute le beacon ", l)
		BS.append(L[2])
	d = abs(L[0] - L[2]) + abs(L[1] - L[3]) #distance
	if -d + abs(L[1] - y_search) < d - abs(L[1] - y_search) + 1 :
		P.append([L[0] - d + abs(L[1] - y_search), L[0] + d - abs(L[1] - y_search)])


P.sort(key=lambda x : x[0])

total = 0
current_xmin = P[0][0]
while len(P) != 0 :
	current_elem = P[0]
	total+= current_elem[1] - current_xmin + 1
	current_xmin = current_elem[1] + 1
	while len(P) != 0 :
		e = P[0]
		if e[1] < current_xmin :
			P.remove(e)
		else :
			break

print(total - len(BS))
