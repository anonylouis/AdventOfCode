#!/usr/bin/python3

f = open('input.txt')

ranges = f.readline()[:-1].split(',')

s = 0
for r in ranges :
    start, end = list(map(int, r.split('-')))
    for i in range(start, end + 1) :
        i_str = str(i)
        n = len(i_str)
        for p in range(1, n // 2 + 1) :
            if n % p == 0 :
                pattern = str(i % (10 ** p))
                if i_str == (pattern * (n // p)) :
                    s += i
                    break

print(s)