#!/usr/bin/python3

f = open('input.txt')

## box = [X, Y, Z, circuit]
boxes = [list(map(int, line[:-1].split(','))) for line in f.readlines()]
for i in range(len(boxes)) :
    boxes[i].append(i)

get_distance = lambda x, y : (x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2

distances = []
for i in range(len(boxes)) :
    for j in range(i + 1, len(boxes)) :
        distances.append([get_distance(boxes[i], boxes[j]), i, j])

distances.sort(reverse=True)

while True :
    if len(distances) == 0 :
        break
    shortest = distances.pop()
    box1, box2 = boxes[shortest[1]], boxes[shortest[2]]
    if (box1[3] == box2[3]) :
        continue

    new_circuit, old_circuit = box1[3], box2[3]
    if new_circuit > old_circuit :
        old_circuit, new_circuit = new_circuit, old_circuit
    for box in boxes :
        if box[3] == old_circuit :
            box[3] = new_circuit

    circuits = set([box[3] for box in boxes])
    if (len(circuits) == 1) :
        print(box1[0] * box2[0])
        break 

