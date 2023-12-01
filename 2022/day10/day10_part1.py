#!/usr/bin/python3

f = open('input.txt')

X, c = 1, 1
L=[]
for l in f :
	l = (l[:-1]).split()
	if l[0] == "noop" :
		c+=1
	else :
		c+=1
		if c in [20,60,100,140,180,220] :
			L.append(X*c)
		X+=int(l[1])
		c+=1
	if c in [20,60,100,140,180,220] :
		L.append(X*c)

print(sum(L))