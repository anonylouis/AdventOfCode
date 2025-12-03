#!/usr/bin/python3

f = open('input.txt')

s = 0
DIGITS = 12

for line in f :
    batteries = list(map(int, line[:-1]))
    joltage, index = [], []
    
    joltage.append((max(batteries[:(1 - DIGITS)])))
    index.append(batteries.index(joltage[-1]))
    for d in range(2 - DIGITS, 0) :
        joltage.append(max(batteries[index[-1] + 1: d]))
        index.append(index[-1] + 1 + batteries[index[-1] + 1: d].index(joltage[-1]))
    joltage.append(max(batteries[index[-1] + 1:]))
    
    s += int("".join(map(str, joltage)))

print(s)