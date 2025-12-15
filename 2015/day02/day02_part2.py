#!/usr/bin/python3

ribbon = 0
for line in open('input.txt') :
    dim = list(map(int, line[:-1].split("x")))
    dim.sort()
    ribbon += 2 * (dim[0] + dim[1]) + dim[0] * dim[1] * dim[2]
 
print(ribbon)