#!/usr/bin/python3

f = open('input.txt')

connections = {}

def addConnection(_str1, _str2) :
    global connections
    if _str1 not in connections :
        connections[_str1] = set()
    connections[_str1].add(_str2)

for line in f :
    line = line[:-1].split('-')
    addConnection(line[0], line[1])
    addConnection(line[1], line[0])
    
trios = set()
for connection1 in connections.keys() :
    if connection1[0] == 't' :
        for connection2 in connections[connection1] :
            for connection3 in connections[connection1] :
                if connection2 != connection3 and connection2 in connections[connection3] :
                    trios.add('-'.join(sorted([connection1, connection2, connection3])))

print(len(trios))