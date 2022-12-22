#!/usr/bin/python3

f = open('input.txt')

M = []
pos = []
facing = 0

for l in f :
	if l == "\n" :
		break
	if pos == [] and "." in l :
		pos = [len(M), l.find('.')]
	M.append(l[:-1])

path = f.readline()

print(pos)
print(path)

def print_map(M, pos) :
	for k in range(len(M)) :
		for l in range(len(M[k])) :
			if k==pos[0] and l==pos[1] :
				print("A", end="")
			else :
				print(M[k][l], end="")
		print()
	print()

current = ""
for i in path :
	if i != "R" and i != "L" and i != "\n":
		current+=i
	else :
		print(current, facing)
		current = int(current)
		for j in range(current) :
			if facing == 0 : # >>
				if len(M[pos[0]]) == pos[1] + 1 :
					pos[1] = M[pos[0]].find('.')
				elif M[pos[0]][pos[1] + 1] == '.' :
					pos[1] += 1
			elif facing == 1 : # vv
				if len(M) == pos[0] + 1 or len(M[pos[0] + 1]) <= pos[1] or M[pos[0] + 1][pos[1]] == ' ':
					save = pos[0]
					while (pos[0] > 0 and len(M[pos[0] - 1]) >= pos[1] and  M[pos[0] - 1][pos[1]] != ' '):
						pos[0] -= 1
					if M[pos[0]][pos[1]] == '#' :
						pos[0] = save
					else :
						while (M[pos[0]][pos[1]] != '.') :
							pos[0] +=1
				elif M[pos[0] + 1][pos[1]] == '.' :
					pos[0] += 1
			elif facing == 2 : # <<
				if pos[1] == 0 or M[pos[0]][pos[1]] == ' ':
					pos[1] = M[pos[0]].rfind('.')
				elif M[pos[0]][pos[1] - 1] == '.' :
					pos[1] -= 1
			else : # ^^
				if pos[0] == 0 or len(M[pos[0] - 1]) <= pos[1] or M[pos[0] - 1][pos[1]] == ' ':
					save = pos[0]
					while (pos[0] > len(M) and len(M[pos[0] + 1]) >= pos[1] and  M[pos[0] + 1][pos[1]] != ' '):
						pos[0] += 1
					if M[pos[0]][pos[1]] == '#' :
						pos[0] = save
					else :
						while (M[pos[0]][pos[1]] != '.') :
							pos[0] -=1
				elif M[pos[0] - 1][pos[1]] == '.' :
					pos[1] -= 1
			if (current == 9 and facing== 3):
				print_map(M, pos)
			#print_map(M, pos)

		if (i == "R") :
			facing = (facing + 1) % 4
		elif (i =="L") :
			facing = (facing - 1) % 4
		current=""

print(pos)
	
print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)