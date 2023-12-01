#!/usr/bin/python3

f = open('input.txt')

cubes = set()
surface = 0

for l in f :
	x,y,z =	list(map(int, l[:-1].split(',')))
	n = 6
	if (x - 1, y , z) in cubes :
		n-=1
		surface-=1
	if (x + 1, y , z) in cubes :
		n-=1
		surface-=1
	if (x , y - 1, z) in cubes :
		n-=1
		surface-=1
	if (x , y + 1, z) in cubes :
		n-=1
		surface-=1
	if (x , y, z - 1) in cubes :
		n-=1
		surface-=1
	if (x , y, z + 1) in cubes :
		n-=1
		surface-=1
	cubes.add((x,y,z))
	surface+=n

print(surface)