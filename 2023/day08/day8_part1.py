#!/usr/bin/python3

f = open('input.txt')

instructions = f.readline()[:-1]
f.readline()
M = {}

for l in f :
	l = l[:-1].replace(',', '').replace('(','').replace(')', '').replace('=','').split()
	M[l[0]] = [l[1], l[2]]

current = "AAA"
step = 0
while(current != "ZZZ") :
	if (instructions[step % len(instructions)] == 'R') :
		current = M[current][1]
	else :
		current = M[current][0]
	step += 1

print(step)