#!/usr/bin/python3

D =  {}

f = open('input.txt')
for l in f :
	D[l[:4]] = l[6:-1]

def f(p) :
	r = D[p]
	if '+' in r :
		L = r.replace("+", " ").split()
		return f(L[0]) + f(L[1])
	elif '*'  in r :
		L = r.replace("*", " ").split()
		return f(L[0]) * f(L[1])
	elif '/' in r :
		L = r.replace("/", " ").split()
		return f(L[0]) // f(L[1])
	elif '-' in r :
		L = r.replace("-", " ").split()
		return f(L[0]) - f(L[1])
	else :
		return int(r)

print(f("root"))