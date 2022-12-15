#!/usr/bin/python3

f = open('input.txt')

xmin, xmax, ymin, ymax = -1, -1, -1, -1
C=[]

for l in f :
	L=l[:-1].replace("=", " ").replace(",", " ").replace(":", " ").split()
	L = list(map(int, [L[3], L[5], L[11], L[13]]))
	L.append(abs(L[0] - L[2]) + abs(L[1] - L[3]))
	C.append(L)
	X, Y = [L[0] - L[4], L[0] + L[4]], [L[1] - L[4], L[1] + L[4]]
	xmin = min(X) if xmin==-1 or min(X) < xmin else xmin
	xmax = max(X) if xmax==-1 or max(X) > xmax else xmax
	ymin = min(Y) if ymin==-1 or min(Y) < ymin else ymin
	ymax = max(Y) if ymax==-1 or max(Y) > ymax else ymax

print(xmin, xmax, ymin, ymax)

M = [[0 for i in range(xmax - xmin + 1)] for j in range(ymax - ymin + 1)]
# 0 for possible position of beacon
# 1 for not possible position of beacon
# 2 for signal
# 3 for beacon

for S in C :
	M[S[1] - ymin][S[0] - xmin] = 2 #signal
	M[S[3] - ymin][S[2] - xmin] = 3 #beacon
	d = S[4] #distance
	print(d)
	for x in range(-1 * d, d + 1) :
		for y in range(-d + abs(x), d - abs(x) + 1) :
			px,py = S[0] + x, S[1] + y
			if M[py - ymin][px - xmin]  == 0 :
				M[py - ymin][px - xmin] = 1

#for i in M :
 	#print(i)

#print(M[10 - ymin])
print(sum([i == 1 for i in M[2000000 - ymin]]))
	# for x in range(2 * d) :
	# 	for y in range()
	# 	if x >= xmin and x <= xmax :



# for i in M :
# 	print(i)