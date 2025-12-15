#!/usr/bin/python3

i, j = 0, 0
houses = set()
houses.add((i, j))

for l in open('input.txt').readline()[:-1] :
    if l == "^" : j += 1
    elif l == "<" : i -= 1
    elif l == ">" : i += 1
    elif l == "v" : j -= 1
    houses.add((i,j))

print(len(houses))
 