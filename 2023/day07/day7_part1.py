#!/usr/bin/python3

from functools import cmp_to_key

f = open('input.txt')

H = []
for l in f :
	l = l[:-1].split()
	H.append([l[0], int(l[1])])

order = "23456789TJQKA"

def cmp(hand1, hand2):
	a = hand1[0]
	b = hand2[0]
	c1 = [a.count(i) for i in set(a)]
	c2 = [b.count(i) for i in set(b)]
	n = max(c1) - max(c2)
	if (n != 0) :
		return n
	elif (max(c1) == 3 or max(c1) == 2) :
		n = len(c2) - len(c1)
		if (n != 0) :
			return n
	for i in range(5) :
		n = order.index(a[i]) - order.index(b[i])
		if (n != 0) :
			return n
	return 0

H = sorted(H, key=cmp_to_key(cmp))

print(sum([(i + 1) * H[i][1] for i in range(len(H))]))
