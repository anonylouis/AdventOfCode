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
		return f(L[0]) / f(L[1])
	elif '-' in r :
		L = r.replace("-", " ").split()
		return f(L[0]) - f(L[1])
	else :
		return int(r)

def dependsOfHumn(p) :
	if (p == "humn") :
		return True
	r = D[p]
	if '+' in r :
		L = r.replace("+", " ").split()
		return dependsOfHumn(L[0]) or dependsOfHumn(L[1])
	elif '*'  in r :
		L = r.replace("*", " ").split()
		return dependsOfHumn(L[0]) or dependsOfHumn(L[1])
	elif '/' in r :
		L = r.replace("/", " ").split()
		return dependsOfHumn(L[0]) or dependsOfHumn(L[1])
	elif '-' in r :
		L = r.replace("-", " ").split()
		return dependsOfHumn(L[0]) or dependsOfHumn(L[1])
	else :
		return False

def result(p, goal) :
	if (p == "humn") :
		return int(goal)
	else :
		r = D[p]
		if '+' in r :
			L = r.replace("+", " ").split()
			if dependsOfHumn(L[0]) and not dependsOfHumn(L[1]):
				return (result(L[0], goal - f(L[1])))
			return (result(L[1], goal - f(L[0])))
		elif '*'  in r :
			L = r.replace("*", " ").split()
			if dependsOfHumn(L[0]) and not dependsOfHumn(L[1]):
				return (result(L[0], goal / f(L[1])))
			return (result(L[1], goal / f(L[0])))
		elif '/' in r :
			L = r.replace("/", " ").split()
			if dependsOfHumn(L[0]) and not dependsOfHumn(L[1]):
				return (result(L[0], goal * f(L[1])))
			return (result(L[1], goal * f(L[0])))
		elif '-' in r :
			L = r.replace("-", " ").split()
			if dependsOfHumn(L[0]) and not dependsOfHumn(L[1]):
				return (result(L[0], goal + f(L[1])))
			return (result(L[1], f(L[0]) - goal))

monkey1, monkey2 = D["root"].replace("+", " ").replace("-", " ").replace("/", " ").replace("*", " ").split()

if dependsOfHumn(monkey1) :
	print(result(monkey1, f(monkey2)))
else :
	print(result(monkey2, f(monkey1)))