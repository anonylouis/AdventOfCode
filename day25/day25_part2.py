#!/usr/bin/python3

base = {"2":2, "1":1, "0":0, "-":-1, "=":-2}

def SNAFU_to_decimal(n) :
	res = 0
	p = 1
	for c in n[::-1] :
		res += base[c] * p
		p *= 5
	return (res)

def decimal_to_SNAFU(n) :
	res = ""
	rest = 0
	while (n != 0 or res == "" or rest != 0) :
		rest += n % 5
		if (rest%5) < 3 :
			res += str(rest % 5)
			rest //= 5
		elif (rest%5) == 3 :
			res += "="
			rest //= 5
			rest += 1
		elif (rest%5) == 4 :
			res += "-"
			rest //= 5
			rest += 1
		n //= 5

	return (res[::-1])

f = open('input.txt')
s = 0
for l in f :
	s += SNAFU_to_decimal(l[:-1])

print(decimal_to_SNAFU(s))