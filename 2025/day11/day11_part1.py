#!/usr/bin/python3

f = open('input.txt')

graph = {}

for line in f :
    line = line[:-1].replace(':', ' ').split()
    graph[line[0]] = line[1:]

nb_path = 0
visited = set()
def dfs(node, goal) :
    global nb_path, graph, visited
    if node in visited :
        return
    if node == goal :
        nb_path += 1
        return
    visited.add(node)
    for next_node in graph[node] :
        dfs(next_node, goal)
    visited.remove(node)
    
dfs('you', 'out')

print(nb_path)