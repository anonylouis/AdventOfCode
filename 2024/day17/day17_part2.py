#!/usr/bin/python3
 
lines = open('input.txt').readlines()
program = list(map(int, lines[4].split(": ")[1].split(',')))[::-1]

A = 0
## backtracking
def solver(_A = "", _nb = 0) :
	global A
	if _nb >= len(program) :
		A = _A
		return True 
	for i in range(8) :
		test_A = _A + '{0:03b}'.format(i)
		tmp = (int(test_A, 2) % 8) ^ 5 
		tmp = (tmp ^ 6 ^ int(int(test_A, 2) / 2**tmp)) % 8
		if tmp == program[_nb] :
			if (solver(test_A, _nb + 1)) :
				return True
	return False

solver()
print(int(A, 2))