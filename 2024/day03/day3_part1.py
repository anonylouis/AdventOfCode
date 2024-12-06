#!/usr/bin/python3
import re

f = open('input.txt')

s = 0
pattern = r'mul\(\d{1,3},\d{1,3}\)'

for line in f :
	matchs = re.findall(pattern, line)
	for match in matchs : 
		a, b = map(int, match[4:-1].split(','))
		s += a * b

print(s)
