#!/usr/bin/python3

f = open('input.txt')

graph = {}

for line in f :
    line = line[:-1].replace(':', ' ').split()
    graph[line[0]] = line[1:]

visited = set()
def dfs(node, goal, paths = [], excludedNodes = ['out']) :
    global graph, visited
    if node in visited:
        return paths
    if node == goal :
        paths.append([v for v in visited] + [ node ])
        return paths
    if node in excludedNodes :
        return paths
    visited.add(node)
    for next_node in graph[node] :
        dfs(next_node, goal, paths)
    visited.remove(node)
    return paths
    
partial_paths = dfs('dac', 'out')
partial_paths = [path for path in partial_paths if 'svr' not in path]
print(len(partial_paths))

print(visited)
for path in partial_paths :
    print(len(dfs('fft', 'dac', excludedNodes=path)))



print(partial_paths[0])
