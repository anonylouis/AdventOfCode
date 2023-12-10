#!/usr/bin/python3.9

import math
from functools import reduce

f = open('input.txt')

instructions = f.readline()[:-1]
f.readline()
M = {}
test = 16306
for l in f :
	l = l[:-1].replace(',', '').replace('(','').replace(')', '').replace('=','').split()
	M[l[0]] = [l[1], l[2]]

def find_circle(_current) :
	_step = 0
	circle = []
	while (1) :
		if (instructions[_step % len(instructions)] == 'R') :
			_current = M[_current][1]
		else :
			_current = M[_current][0]
		if (_step % len(instructions) == 0) :
			if _current not in circle :
				circle.append(_current)
			else :
				return [circle.index(_current) * len(instructions), (len(circle) - circle.index(_current)) * len(instructions)]
		_step +=1

def find_index_Z(_current, _skip, _rot) :
	_step = 0
	_index = []
	while (1) :
		if (instructions[_step % len(instructions)] == 'R') :
			_current = M[_current][1]
		else :
			_current = M[_current][0]
		if (_step >= _skip and _current[-1] == 'Z') :
			_index.append(_step - _skip)
		if (_step > _skip and (_step - _skip) % _rot == 0) :
				return _index
		_step +=1

index_Z = []
current = [k for k in M.keys() if k[-1] == 'A']
skip, rot = [], []
for c in current :
	tmp1, tmp2 = find_circle(c)
	skip.append(tmp1)
	rot.append(tmp2)
	for index in find_index_Z(c, tmp1, tmp2) :
		index_Z.append(index)

print(skip)
print(rot)
t = 1
for i in index_Z :
	t = math.lcm(t, i)
print(t)