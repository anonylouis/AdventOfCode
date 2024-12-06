#!/usr/bin/python3
 
f = open('input.txt')

rules = []
parseRule = True
s = 0

for line in f :
	if line == "\n" :
		parseRule = False
	elif parseRule :
		line = list(map(int, line[:-1].split('|')))
		rules.append(line)
	else :
		order = list(map(int, line[:-1].split(',')))
		valid = True
		for rule in rules :
			a, b = rule
			try :
				index_a, index_b = order.index(a), order.index(b)
				if index_a > index_b :
					valid = False
					break
			except ValueError:
				pass
		if valid :
			s += order[len(order) //2]

print(s)