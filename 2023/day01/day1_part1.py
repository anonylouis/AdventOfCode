#!/usr/bin/python3

f = open('input.txt')

s = 0
for line in f :
	digits = [i for i in line if i.isdigit()]
	s += int(digits[0]+digits[-1])
print(s)