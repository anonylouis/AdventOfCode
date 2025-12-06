#!/usr/bin/python3

f = open('input.txt')
lines = f.readlines()

operations = lines.pop()[:-1].split()
numbers = [list(map(int, l[:-1].split())) for l in lines]

total = 0
for i in range(len(operations)) :
    if operations[i] == "+" :
        r = 0
        for number in numbers :
            r += number[i]
    else :
        r = 1
        for number in numbers :
            r *= number[i]
    total += r

print(total)
