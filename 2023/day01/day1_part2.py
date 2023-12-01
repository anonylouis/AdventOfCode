#!/usr/bin/python3

f = open('input.txt')

number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

s = 0
for line in f :
	digits = []
	for i in range(len(line)) :
		if line[i].isdigit() :
			digits += line[i]
		elif any([line[i:].startswith(n) for n in number]) :
			digits += str([line[i:].startswith(n) for n in number].index(True) + 1)
	s += int(digits[0]+digits[-1])
print(s)