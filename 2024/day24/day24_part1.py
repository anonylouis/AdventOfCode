#!/usr/bin/python3

f = open('input.txt')

operations = {"AND": 0, "OR": 1, "XOR": 2}
vars = {}

# array of [var1, var2, op, result]
L = []

parse_vars = True
for line in f :
    if line == '\n' :
        parse_vars = False
    elif parse_vars :
        line = line[:-1].split(': ')
        vars[line[0]] = int(line[1])
    else :
        line = line[:-1].split()
        L.append([line[0], line[2], operations[line[1]], line[4]])

while len(L) != 0 :
    next_L = []
    for e in L :
        if e[0] in vars and e[1] in vars :
            if e[2] == 0 : vars[e[3]] = vars[e[0]] & vars[e[1]]
            if e[2] == 1 : vars[e[3]] = vars[e[0]] | vars[e[1]]
            if e[2] == 2 : vars[e[3]] = vars[e[0]] ^ vars[e[1]]
        else :
            next_L.append(e)
    L = next_L

zWires = sorted([k for k in vars.keys() if k[0] == 'z'])
print(int(''.join([str(vars[k]) for k in zWires][::-1]), 2))
