#!/usr/bin/python3

f = open('input.txt')
width = 7

#one line with the floor of the cave
C = [[1 for i in range(width)]]

jet = f.readline()
i_jet = -1

i_rock = -1
# 0 = - shape
# 1 =  + shape
# 2 = L inverted shape
# 3 = | shape
# 4 = squre shape

current = 0
t = 0
nb_rock = 0

while nb_rock != 2022 :
	if t % 2 == 0 : 
		if (current == 0) : #new rock
			i_rock = (i_rock + 1) % 5
			if (i_rock == 0) :
				current = [[1,1,1,1], 2, 3]
			elif (i_rock == 1) :
				current = [[0, 1, 0], [1, 1, 1], [0, 1, 0], 2, 3]
			elif (i_rock == 2) :
				current = [[1, 1, 1], [0, 0, 1], [0, 0, 1], 2, 3]
			elif (i_rock == 3) :
				current = [[1], [1], [1], [1], 2, 3]
			else :
				current = [[1, 1], [1, 1], 2, 3]
		else : #current falling
			if (current[-1] > 0) :
				current[-1] -= 1
			else :
				v = 1
				if i_rock == 1 : # + shape
					if current[-1] == 0 :
						if C[-1][current[-2] + 1] == 1 :
							v = 0
					elif C[current[-1] - 1][current[-2] + 1] == 1  or C[current[-1]][current[-2]] == 1 or C[current[-1]][current[-2]+2] == 1 :
							v = 0
				else :
					for i in range(len(current[0])) :
						if (current[0][i] + C[current[-1] - 1][current[-2] + i]) > 1 :
							v = 0
							break
				if v == 1 :
					current[-1] -= 1
				else :
					for i in range(len(current) - 2) :
						if current[-1] >= 0 :
							line = current[-2] * [0] + current[i]
							line += [0] * (7 - len(line))
							C.append(line)
						else :
							for j in range(len(current[i])) :
								if current[i][j] == 1 :
									C[current[-1]][current[-2] + j] = current[i][j]
							current[-1] += 1
					current = 0
					nb_rock += 1
					continue
	else :
		i_jet = (i_jet + 1) % len(jet)
		if current[-1] >= 0 :
			if jet[i_jet] == '>' :
				if current[-2] + len(current[0]) < 7 :
					current[-2] += 1
			else :
				if current[-2] > 0 :
					current[-2] -= 1
		else :
			v = 1
			if jet[i_jet] == '>' :
				if current[-2] + len(current[0]) == 7 :
					v = 0
				else :
					j = current[-1]
					for i in range(0, len(current) - 2) :
						if j >= 0 :
							break
						if (max([current[i][k] + C[j][current[-2]+k+1] for k in range(len(current[i]) - 1, -1, -1)]) > 1) :
							v = 0
							break
						j+=1
				if v == 1 :
					current[-2] += 1
			else :
				if current[-2] == 0 :
					v = 0
				else :
					j = current[-1]
					for i in range(0, len(current) - 2) :
						if j >= 0 :
							break
						if (max([current[i][k] + C[j][current[-2]-1+k] for k in range(len(current[i]))]) > 1) :
							v = 0
							break
						j+=1
				if v == 1 :
					current[-2] -= 1
	t+=1

print(len(C) - 1)