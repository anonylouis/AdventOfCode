#!/usr/bin/python3

f = open('input.txt')

s = 0

for line in f :
    batteries = list(map(int, line[:-1]))
    a = max(batteries[:-1])
    b = max(batteries[batteries.index(a) + 1:])
    s += a * 10 + b

print(s)