#!/usr/bin/python3

floor = 0
for i, v in enumerate(open('input.txt').readline()[:-1]) :
    if v == "(" :
        floor += 1
    elif  v == ")" :
        floor -= 1
    
    if floor == -1 :
        print(i + 1)
        break

