#!/usr/bin/python3
from enum import Enum
import copy

f = open('input.txt')

M=[]
position_original=[]
c = 0

class Direction(Enum):
    TOP    = 1
    DOWN   = 2
    LEFT   = 3
    RIGHT  = 4

for line in f :
	if len(position_original) == 0 and line.find('^') >= 0 : 
		position_original = [line.find('^'), len(M), Direction.TOP]
	M.append(list(line[:-1]))

def print_map() :
	print("")
	for line in M :
		print(line)
	print("")

limits = [len(M[0]) - 1, len(M) - 1]

def get_path(position_original) : 
	global c
	path  = []
	position = position_original
	while True :
		X, Y = position[0], position[1]
		direction = position[2]
		if X < 0 or Y < 0 or X > limits[0] or Y > limits[1] :
			return path

		if position not in path :
			path.append(position)
		else :
			#print("obstacle en ", i, j)
			c += 1
			return path
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

path_original = get_path(position_original)
path_original = set([(p[0], p[1]) for p in path_original])
print(len(path_original))
for p in path_original :
	i, j = p[1], p[0]
	if M[i][j] == '.' :
		M[i][j] = '#'
		get_path(position_original)
		M[i][j] = '.'

print(c)