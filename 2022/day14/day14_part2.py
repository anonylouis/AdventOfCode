#!/usr/bin/python3

f = open('input.txt')

xmin, xmax, ymin, ymax = -1, -1, -1, -1
parsing = lambda x : list(map(int, x.split(",")))

R=[]
for l in f :
	L=list(map(parsing, l[:-1].replace("->", " ").split()))
	R.append(L)
	X, Y = [e[0] for e in L], [e[1] for e in L]
	xmin = min(X) if xmin==-1 or min(X) < xmin else xmin
	xmax = max(X) if xmax==-1 or max(X) > xmax else xmax
	ymin = min(Y) if ymin==-1 or min(Y) < ymin else ymin
	ymax = max(Y) if ymax==-1 or max(Y) > ymax else ymax

sand_overflow = ymax
cave = [[0 for i in range(xmax - xmin + 1 + 2 * sand_overflow)] for j in range(ymax + 3)]
for r in R :
	x, y = r[0]
	for l in r[1:] :
		while x < l[0] :
			cave[y][x - xmin + sand_overflow] = 1
			x+=1
		while x > l[0] :
			cave[y][x - xmin + sand_overflow] = 1
			x-=1
		while y < l[1] :
			cave[y][x - xmin + sand_overflow] = 1
			y+=1
		while y > l[1] :
			cave[y][x - xmin + sand_overflow] = 1
			y-=1
		cave[y][x - xmin + sand_overflow] = 1

#floor
for i in range(len(cave[-1])) :
	cave[-1][i] = 1

n = 0
while 1 :
	sx, sy = 500 - xmin + sand_overflow, 0
	while 1 :
		if cave[sy + 1][sx] == 0 :
			sy += 1
		elif cave[sy + 1][sx - 1] == 0 :
			sy += 1
			sx -= 1
		elif cave[sy + 1][sx + 1] == 0 :
			sy += 1
			sx += 1
		else :
			n+=1
			cave[sy][sx] = 2
			if sx == 500 - xmin + sand_overflow and sy == 0 :
				print(n)
				exit()
			break
