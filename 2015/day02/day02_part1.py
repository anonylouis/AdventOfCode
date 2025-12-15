#!/usr/bin/python3

wrapping = 0
for line in open('input.txt') :
    l, v, w = map(int, line[:-1].split("x"))
    wrapping += 2 * (l * v + v * w +  l * w) + min(l * v, v * w, l * w)

print(wrapping)