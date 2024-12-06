#!/usr/bin/python3
from enum import Enum

f = open('input.txt')

M=[]
position=[]
class Direction(Enum):
    TOP    = 1
    DOWN   = 2
    LEFT   = 3
    RIGHT  = 4

for line in f :
	if len(position) == 0 and line.find('^') >= 0 : 
		position = [line.find('^'), len(M), Direction.TOP]
	M.append(list(line[:-1]))

limits = [len(M[0]) - 1, len(M) - 1]

while True :
	X, Y = position[0], position[1]
	direction = position[2]
	if X < 0 or Y < 0 or X > limits[0] or Y > limits[1] :
		break
	M[Y][X] = "X"
	if direction == Direction.TOP :
		if Y == 0 or M[Y - 1][X] != "#" :
			Y = Y - 1
		else :
			direction = Direction.RIGHT
	elif direction == Direction.RIGHT :
		if X == limits[0] or M[Y][X + 1] != "#" :
			X = X + 1
		else :
			direction = Direction.DOWN
	elif direction == Direction.DOWN :
		if Y == limits[1] or M[Y + 1][X] != "#" :
			Y = Y + 1
		else :
			direction = Direction.LEFT
	elif direction == Direction.LEFT :
		if X == 0 or M[Y][X - 1] != "#" :
			X = X - 1
		else :
			direction = Direction.TOP
	position = [X, Y, direction]

print(sum([line.count('X') for line in M]))