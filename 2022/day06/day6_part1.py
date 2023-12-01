#!/usr/bin/python3

f = open('input.txt')

l = f.readline()
for i in range(4, len(l)) :
	L = set([l[j] for j in range(i - 3, i +1)])
	if (len(L)  == 4) :
		print(i + 1)
		break