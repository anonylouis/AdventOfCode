#!/usr/bin/python3
import re

f = open('input.txt')

s = 0
enable = True
pattern = r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))'

for line in f :
	matchs = re.findall(pattern, line)
	print(matchs)
	for match in matchs :
		if match == "do()" :
			enable = True
		elif match == "don't()" :
			enable = False
		elif enable:
			a, b = map(int, match[4:-1].split(','))
			s += a * b

print(s)
