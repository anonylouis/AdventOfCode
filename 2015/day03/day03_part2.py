#!/usr/bin/python3

coords = [[0, 0], [0, 0]]

houses = set()
houses.add((0, 0))

for i, v in enumerate(list(open('input.txt').readline()[:-1])) :
    if v == "^" : coords[i % 2][1] += 1
    elif v == "<" : coords[i % 2][0] -= 1
    elif v == ">" : coords[i % 2][0] += 1
    elif v == "v" : coords[i % 2][1] -= 1

    houses.add(tuple(coords[0]))
    houses.add(tuple(coords[1]))

print(len(houses))
 