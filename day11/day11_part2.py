#!/usr/bin/python3

f = open('input.txt')

M=[]
current=[]

for l in f :
	l = l[:-1].replace(',',' ').split()
	if (len(l) == 0 or l[0] == "Monkey") :
		continue
	elif (l[0] == "Starting") :
		L = [int(l[i]) for i in range(2, len(l))]
		current.append(L)
	elif (l[0] == "Operation:") :
		current.append([l[-3], l[-2], l[-1]])
	elif (l[0] == "Test:") :
		current.append(int(l[-1]))
	elif (l[0] == "If" and l[1] == "true:") :
		current.append(int(l[-1]))
	elif (l[0] == "If" and l[1] == "false:") :
		current.append(int(l[-1]))
		current.append(0)
		M.append(current)
		current = []
	
#print(M)
s = 1
for i in [M[k][2] for k in range(0, len(M))] :
	s*=i

for i in range(1, 10001) :
	for j in range(len(M)) :
		monkey = M[j]
		while (len(monkey[0]) > 0) :
			item = monkey[0].pop(0)
			a = item if monkey[1][0] == "old" else int(monkey[1][0])
			b = item if monkey[1][2] == "old" else int(monkey[1][2])
			if (monkey[1][1] == "*") :
				item = a * b
			elif (monkey[1][1] == "+") :
				item = a + b
			item %= s
			if (item % monkey[2]) == 0 :
				M[monkey[3]][0].append(item)
			else :
				M[monkey[4]][0].append(item)
			monkey[5]+=1

max=[M[k][5] for k in range(0, len(M))]
max.sort()
print(max[-1] * max[-2])
