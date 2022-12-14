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


sand_overflow =  (xmax - xmin) // 2 + 1 
cave = [[0 for i in range(xmax - xmin + 1)] for j in range(ymax - ymin + 1 + sand_overflow)]
for r in R :
	x, y = r[0]
	for l in r[1:] :
		while x < l[0] :
			cave[y - ymin + sand_overflow][x - xmin] = 1
			x+=1
		while x > l[0] :
			cave[y - ymin + sand_overflow][x - xmin] = 1
			x-=1
		while y < l[1] :
			cave[y - ymin + sand_overflow][x - xmin] = 1
			y+=1
		while y > l[1] :
			cave[y - ymin + sand_overflow][x - xmin] = 1
			y-=1
		cave[y - ymin + sand_overflow][x - xmin] = 1


n = 0
while 1 :
	sx, sy = 500 - xmin, 0
	while 1 :
		if (sy + 1) >= len(cave) :
			print(n)
			exit()
		elif cave[sy + 1][sx] == 0 :
			sy += 1
		elif (sx - 1) < 0 :
			print(n)
			exit()
		elif cave[sy + 1][sx - 1] == 0 :
			sy += 1
			sx -= 1
		elif (sx + 1) >= len(cave[0]) :
			print(n)
			exit()
		elif cave[sy + 1][sx + 1] == 0 :
			sy += 1
			sx += 1
		else :
			n+=1
			cave[sy][sx] = 2
			break
