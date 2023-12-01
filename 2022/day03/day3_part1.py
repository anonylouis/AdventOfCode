#!/usr/bin/python3

f = open('input.txt')

s = 0
for l in f :
	l = l[:-1]
	line1, line2 = l[:len(l)//2], l[len(l)//2:]
	for i in line1 :
		if i in line2 :
			print(i, end=" ")
			if i.islower() :
				s+=ord(i) - ord('a') + 1
			else :
				s+=ord(i) - ord('A') + 27
			break
		

print(s)