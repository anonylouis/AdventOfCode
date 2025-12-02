#!/usr/bin/python3

f = open('input.txt')

ranges = f.readline()[:-1].split(',')

s = 0
for r in ranges :
    start, end = list(map(int, r.split('-')))
    for i in range(start, end + 1) :
        n = len(str(i))
        if n % 2 == 0 :
            divisor = 10 ** (n // 2)
            a, b = i % divisor, i // divisor
            if a == b :
                s += i

print(s)