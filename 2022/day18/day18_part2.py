#!/usr/bin/python3
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

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

X = [e[0] for e in cubes]
Y = [e[1] for e in cubes]
Z = [e[2] for e in cubes]
x_min, x_max = min(X), max(X)
y_min, y_max = min(Y), max(Y)
z_min, z_max = min(Z), max(Z)

trapped_air = []

def is_trapped(e, c, xmax, xmin, ymax, ymin, zmin, zmax, visited) :	
	#print(visited)
	if e in c or e in visited :
		return [True, []]
	if e[0] <= xmin or e[0] >=xmax or e[1] <= ymin or e[1] >=ymax or  e[2] <= zmin or e[2] >=zmax :
		return [False]
	visited.append(e)
	if is_trapped((e[0] - 1, e[1], e[2]), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	if is_trapped((e[0] + 1, e[1], e[2]), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	if is_trapped((e[0], e[1] - 1, e[2]), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	if is_trapped((e[0], e[1] + 1, e[2]), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	if is_trapped((e[0], e[1], e[2] - 1), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	if is_trapped((e[0], e[1], e[2] + 1), c, xmax, xmin, ymax,ymin, zmin, zmax, visited)[0] == False :
		return [False]
	return [True, visited]

air = []

for i in range(x_min, x_max + 1) :
	for j in range(y_min, y_max + 1) :
		for k in range(z_min, z_max + 1) :
			if (i, j ,k) not in cubes and (i,j,k) not in air:
					print("testing ",i,j,k)
					v = is_trapped((i,j,k), cubes, x_max, x_min, y_max, y_min, z_min, z_max, [])
					if v[0] == True :
					 	air += v[1]


surface_air = 0
tmp = set()
for e in air :
	x,y,z =	e
	n = 6
	if (x - 1, y , z) in tmp :
		n-=1
		surface_air-=1
	if (x + 1, y , z) in tmp :
		n-=1
		surface_air-=1
	if (x , y - 1, z) in tmp :
		n-=1
		surface_air-=1
	if (x , y + 1, z) in tmp :
		n-=1
		surface_air-=1
	if (x , y, z - 1) in tmp :
		n-=1
		surface_air-=1
	if (x , y, z + 1) in tmp :
		n-=1
		surface_air-=1
	tmp.add((x,y,z))
	surface_air+=n

print(air)
print(surface_air)

print(surface - surface_air)