#!/usr/bin/python3

f = open('input.txt')

X, c = 1, 1
CRT=""
for l in f :
	if ((c - 1)%40) in [X - 1, X, X + 1] :
		CRT+="#"
	else :
		CRT+="."
	if c%40 == 0 :
		CRT+="\n"
	l = (l[:-1]).split()
	if l[0] == "noop" :
		c+=1
	else :
		c+=1
		if ((c - 1)%40) in [X - 1, X, X + 1] :
			CRT+="#"
		else :
			CRT+="."
		if c%40 == 0 :
			CRT+="\n"
		X+=int(l[1])
		c+=1

print(CRT)/Mazoise