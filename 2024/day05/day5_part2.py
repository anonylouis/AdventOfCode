#!/usr/bin/python3
 
f = open('input.txt')

rules = []
parseRule = True
s = 0

def fix_order(_order) :
	valid = False
	while not valid :
		valid = True
		for rule in rules :
			a, b = rule
			try :
				index_a, index_b = order.index(a), order.index(b)
				if index_a > index_b :
					order[index_a], order[index_b] = b, a
					valid = False
					break
			except ValueError:
				pass
	return _order


for line in f :
	if line == "\n" :
		parseRule = False
	elif parseRule :
		line = list(map(int, line[:-1].split('|')))
		rules.append(line)
	else :
		order = list(map(int, line[:-1].split(',')))
		for rule in rules :
			a, b = rule
			try :
				index_a, index_b = order.index(a), order.index(b)
				if index_a > index_b :
					valid = False
					order = fix_order(order)
					s += order[len(order) //2]
					break
			except ValueError:
				pass

print(s)