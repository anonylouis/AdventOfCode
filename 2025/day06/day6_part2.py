#!/usr/bin/python3

f = open('input.txt')
lines = f.readlines()

operations = lines.pop()[:-1]
i_operations = [i for (i, op) in enumerate(operations) if op in "+*"]

numbers = [l[:-1] for l in lines]

total = 0
for i in range(len(i_operations)) :
    operation = operations[i_operations[i]]
    
    min_j = i_operations[i]
    if i != len(i_operations) - 1 :
        max_j = i_operations[i + 1] - 1
    else :
        max_j = len(operations)

    r = 0 if operation == "+" else 1
    for j in range(min_j, max_j) :
        n = int("".join([number[j] for number in numbers]))
        if operation == "+" :
            r += n
        else :
            r *= n
    total += r

print(total)
