#!/usr/bin/python3

f = open('input.txt')

s = 0
for l in f :
	l = l[:-1]
	elves1, elves2 = l.split(",")
	elves1 = list(map(int, elves1.split("-")))
	elves2 = list(map(int, elves2.split("-")))
	if not (elves1[1] < elves2[0] or elves2[1] < elves1[0]) :
		s+=1

print(s)