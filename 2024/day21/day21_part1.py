#!/usr/bin/python3
import re
from itertools import permutations

f = open('input.txt')

numericKeypad = {
	'7' : [0, 0], '8' : [0, 1], '9': [0, 2],
	'4' : [1, 0], '5' : [1, 1], '6': [1, 2],
	'1' : [2, 0], '2' : [2, 1], '3': [2, 2],
				  '0' : [3, 1], 'A': [3, 2],
}

directionalKeypad = {
	              '^' : [0, 1], 'A': [0, 2],
	'<' : [1, 0], 'v' : [1, 1], '>': [1, 2],
}

def isSeqValid(_seq, _keypad) :
	_pos = [_keypad['A'][0], _keypad['A'][1]]
	for i in _seq :
		if i == '<' : _pos[1] -= 1
		if i == '>' : _pos[1] += 1
		if i == '^' : _pos[0] -= 1
		if i == 'v' : _pos[0] += 1
		if _keypad == numericKeypad and _pos == [3, 0] :
			return False
		if _keypad == directionalKeypad and _pos == [0, 0] :
			return False
	return True

def fillMap(_set) :
	_map = {}
	for a in _set.keys() :
		for b in _set.keys() :
			y, x = _set[b][0] - _set[a][0], _set[b][1] - _set[a][1]
			seq = ""
			if y < 0 : seq += (-y) * '^'
			if x > 0 : seq += x * '>'
			if y > 0 : seq += y * 'v'
			if x < 0 : seq += (-x) * '<'
			_map[a + b] = set([''.join(p) + "A" for p in permutations(seq)])
	return _map

numericMap = fillMap(numericKeypad)
directionalMap = fillMap(directionalKeypad)

def translateToSet(code, _set) :
	_map = numericMap
	if _set == directionalKeypad :
		_map = directionalMap
	seqs = [""]
	_code = "A" + code
	for i in range(len(_code) - 1) :
		new_seq = []
		for possibility in _map[_code[i : i + 2]] :
			for seq in seqs :
				new_seq.append(seq + possibility)
		seqs = new_seq
	return [s for s in seqs if isSeqValid(s, _set)]

def keepMinimumStrings(_sequences) :
	minLen = min([len(s) for s in _sequences])
	return [s for s in _sequences if len(s) == minLen]

complexity = 0
for line in f :
	line = line[:-1]
	sequences = translateToSet(line, numericKeypad)

	robot1 = set()
	for sequence in sequences :
		robot1.update(translateToSet(sequence, directionalKeypad))
	robot1 = keepMinimumStrings(robot1)

	robot2 = set()
	for sequence in robot1 :
		robot2.update(translateToSet(sequence, directionalKeypad))
	robot2 = keepMinimumStrings(robot2)

	complexity += len(robot2[0]) * int(re.sub(r'[^\d]', '', line))

print(complexity)