#!/usr/bin/python3
import numpy as np
from pulp import *

f = open('input.txt')

s = 0
for line in f :
    line = line[:-1].split()
    wanted_joltage = list(map(int, line[-1][1:-1].split(',')))
    buttons = [list(map(int, button[1:-1].split(','))) for button in line[1:-1]]

    A = np.zeros((len(wanted_joltage), len(buttons)), dtype=int)
    for i in range(len(buttons)) :
        for j in buttons[i] :
            A[j][i] = 1
    B = np.array([[_] for _ in wanted_joltage], dtype=int)

    prob = LpProblem("find jotage", LpMinimize)
    x_buttons = [pulp.LpVariable(f"button{i}", 0, None, LpInteger) for i in range(len(buttons))]

    prob += pulp.lpSum(x_buttons), "Minimiser_la_somme_de_X"

    for i in range(len(wanted_joltage)) :
        constraint = []
        for j in range(len(buttons)) :
            if i in buttons[j] :
                constraint.append([x_buttons[j]])
        prob += pulp.lpSum(constraint) == wanted_joltage[i]

    prob.solve()
    s += sum([int(v.varValue) for v in prob.variables()])

print(s)