#!/usr/bin/python3

lines = open('input.txt').readlines()

A = int(lines[0].split(": ")[1])
B = int(lines[1].split(": ")[1])
C = int(lines[2].split(": ")[1])

program = list(map(int, lines[4].split(": ")[1].split(',')))

i = 0
output = []

def execute(_opcode, _operand) :
	global A, B, C, i
	_combo = _operand
	if _operand == 4 :	_combo = A
	if _operand == 5 :	_combo = B
	if _operand == 6 :	_combo = C
	
	if _opcode == 0 :
		A = int(A / 2**_combo)
	elif _opcode == 1 :
		B = B ^ _operand
	elif _opcode == 2 :
		B = _combo % 8
	elif _opcode == 4 :
		B = B ^ C
	elif _opcode == 5 :
		output.append(str(_combo % 8))
	elif _opcode == 6 :
		B = int(A / 2**_combo)
	elif _opcode == 7 :
		C = int(A / 2**_combo)
	
	if _opcode == 3 and A != 0 :
		i = _operand
		return 0
	return 2

while i < len(program) :
	i = execute(program[i], program[i + 1]) + i

print(','.join(output))