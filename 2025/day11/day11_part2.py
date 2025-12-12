#!/usr/bin/python3

f = open('input.txt')

graph = {}

for line in f :
    line = line[:-1].replace(':', ' ').split()
    graph[line[0]] = line[1:]

path = []

memory = {'out' : [0, 0, 0, 1]}

def dfs(node) :
    global graph, path, memory
    if node in memory :
        return memory[node]
    elif node in path:
        return [0, 0, 0, 0]
    path.append(node)
    nb_path = [0, 0, 0, 0]
    for next_node in graph[node] :
        r = dfs(next_node)
        if node == 'dac':
            nb_path[0] += r[2]
            nb_path[1] += r[3]
        elif node == 'fft':
            nb_path[0] += r[1]
            nb_path[2] += r[3]
        else :
            nb_path[0] += r[0]
            nb_path[1] += r[1]
            nb_path[2] += r[2]
            nb_path[3] += r[3]
    path.remove(node)
    memory[node] = nb_path
    return nb_path

print(dfs('svr'))
