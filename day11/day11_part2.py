#!/usr/bin/python3

f = open('input.txt')

def plus(c, d) :
	r = 0
	v = ""
	a, b = c, d
	if (len(c) < len(d)) :
		a, b = d, c
	a,b = a[::-1], b[::-1]
	for i in range(len(b)) :
		n = int(b[i]) + int(a[i]) + r
		v+=str(n%10)
		r = (n - n%10) // 10
	for i in range(len(b), len(a)) :
		n = int(a[i]) + r
		v+=str(n%10)
		r = (n - n%10) // 10
	if r != 0 :
		v=v+str(r)[::-1]
	return (v[::-1])

def moins(c, d) :
	r = 0
	v = ""
	a, b = c, d
	if (len(c) < len(d)) :
		a, b = d, c
	a,b = a[::-1], b[::-1]
	for i in range(len(b)) :
		n = int(a[i]) - (int(b[i]) + r)
		if n < 0 :
			n+=10
			r=1
		else :
			r=0
		v+=str(n)
	for i in range(len(b), len(a)) :
		n = int(a[i]) - r
		if n < 0 :
			n+=10
			r=1
		else :
			r=0
		v+=str(n)
	v=v[::-1]
	while v[0] == "0" and len(v) > 1 :
		v=v[1:]
	return (v)

def mult(c, d) :
	t=0
	r = 0
	a, b = c, d
	if (len(c) < len(d)) :
		a, b = d, c
	a,b = a[::-1], b[::-1]

	for i in range(len(b)) :
		v = ""
		r = 0
		for j in range(len(a)) :
			n = (int(b[i]) * int(a[j])) + r
			v+=str(n%10)
			r = (n - n%10) // 10
		if r != 0 :
			v=v+str(r)[::-1]
		v = v[::-1]+"0"*i
		if t == 0 :
			t = v
		else :
			t = plus(t, v)
	return (t)

def sup(c, d) :
	a, b = c, d
	if (len(a) < len(b)) :
		a = "0"*(len(b)-len(a)) + a
	else :
		b = "0"*(len(a)-len(b)) + b
	for i in range(len(a)) :
		k,p = int(a[i]), int(b[i])
		if (k > p) :
			return 1
		elif (k < p) :
			return -1
	return 0


def modulo(a, b) :
	print("debut")
	s = b
	n = sup(moins(a, s), b)
	while n > 0 :
		s = plus(s, b)
		n = sup(moins(a, s), b)
	print("fin")
	if n == 0:
		return True
	return False


def modulo_23(a) :
	c = a
	while sup(c, "91") > 0:
		c = plus(c[:-1], mult(c[-1], "7"))
	if c == "23" or c == "46" or c == "69" :
		return True
	return False

def modulo_19(a) :
	c = a
	while sup(c, "37") > 0:
		c = plus(c[:-1], mult(c[-1], "2"))
	if c == "19" :
		return True
	return False

def modulo_13(a) :
	c = a
	while sup(c, "51") > 0:
		c = plus(c[:-1], mult(c[-1], "4"))
	if c == "13" or c == "26" or c == "39" :
		return True
	return False

def modulo_17(a) :
	c = a
	while sup(c, "50") > 0:
		c = moins(c[:-1], mult(c[-1], "5"))
	if c == "0" or c == "17" or c == "34" :
		return True
	return False

print(modulo_23("23"))
print(modulo_19("19"))
print(modulo_13("13"))
print(modulo_17("17"))



M=[]
current=[]

for l in f :
	l = l[:-1].replace(',',' ').split()
	if (len(l) == 0 or l[0] == "Monkey") :
		continue
	elif (l[0] == "Starting") :
		L = [str(int(l[i])) for i in range(2, len(l))]
		current.append(L)
	elif (l[0] == "Operation:") :
		current.append([l[-3], l[-2], l[-1]])
	elif (l[0] == "Test:") :
		current.append(str(int(l[-1])))
	elif (l[0] == "If" and l[1] == "true:") :
		current.append(int(l[-1]))
	elif (l[0] == "If" and l[1] == "false:") :
		current.append(int(l[-1]))
		current.append(0)
		M.append(current)
		current = []
	
#print(M)

for i in range(1, 21) :
	for j in range(len(M)) :
		monkey = M[j]
		while (len(monkey[0]) > 0) :
			item = monkey[0].pop(0)
			a = item if monkey[1][0] == "old" else monkey[1][0]
			b = item if monkey[1][2] == "old" else monkey[1][2]
			if (monkey[1][1] == "*") :
				item = mult(a, b)
			elif (monkey[1][1] == "+") :
				item = plus(a, b)
			#item //= 3
			if (monkey[2] == "23") :
				test = modulo_23(item)
			elif (monkey[2] == "19") :
				test = modulo_19(item)
			elif (monkey[2] == "13") :
				test = modulo_13(item)
			else :
				test = modulo_17(item)
			if test :
				M[monkey[3]][0].append(item)
			else :
				M[monkey[4]][0].append(item)
			monkey[5]+=1
	#print(i, [M[k][5] for k in range(0, len(M))])

max=[M[k][5] for k in range(0, len(M))]
print(max)
#max.sort()
#print(max[-1] * max[-2])




