#!/usr/bin/python3

f = open('input.txt')

s=0
L=[]
for line in f :
	L.append(line)
	if (len(L) == 3) :
		for i in L[0] :
			if i in L[1] and i in L[2] :
				if i.islower() :
					s+=ord(i) - ord('a') + 1
				else :
					s+=ord(i) - ord('A') + 27
				break
		L=[]
	
print(s)