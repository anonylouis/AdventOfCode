#!/usr/bin/python3

f = open('input.txt')

s = 0

read_ingredients = False
ranges = []
ingredients = []
for line in f :
    if line == "\n" :
        read_ingredients = True
        continue
    if read_ingredients :
        ingredients.append(int(line[:-1]))
    else :
        a, b = map(int, line[:-1].split('-'))
        ranges.append([a, b])

s = 0
for i in ingredients :
    for r in ranges :
        if r[0] <= i and r[1] >= i :
            s += 1
            break

print(s)