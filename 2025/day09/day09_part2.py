#!/usr/bin/python3

f = open('input.txt')

tiles = [list(map(int, line[:-1].split(','))) for line in f.readlines()]
n = len(tiles)

graph = {}
for i in range(n) :
    graph[i] = []
    left = [[tiles[i][0] - tiles[j][0], j] for j in range(n) if j != i and tiles[i][1] == tiles[j][1] and tiles[i][0] > tiles[j][0]]
    if len(left) > 0 :
        left.sort()
        graph[i].append(left[0][1])

    right = [[tiles[j][0] - tiles[i][0], j] for j in range(n) if j != i and tiles[i][1] == tiles[j][1] and tiles[i][0] < tiles[j][0]]
    if len(right) > 0 :
        right.sort()
        graph[i].append(right[0][1])

    top = [[tiles[i][1] - tiles[j][1], j] for j in range(n) if j != i and tiles[i][0] == tiles[j][0] and tiles[i][1] > tiles[j][1]]
    if len(top) > 0 :
        top.sort()
        graph[i].append(top[0][1])
    
    down = [[tiles[j][1] - tiles[i][1], j] for j in range(n) if j != i and tiles[i][0] == tiles[j][0] and tiles[i][1] < tiles[j][1]]
    if len(down) > 0 :
        down.sort()
        graph[i].append(down[0][1])

## DFS

visited = [False for i in range(n)] 
parent = [-1 for i in range(n)]

def dfs(i) :
    global visited, parent
    if (all(visited) and 0 in graph[i]) :
        return True

    for neighbor in graph[i] :
        if visited[neighbor] == False :
            visited[neighbor] = True
            parent[neighbor] = i
            if (dfs(neighbor)) :
                return True
            visited[neighbor] = False
            parent[neighbor] = -1

    return False

visited[0] = True
if not dfs(0) :
    raise("bad input")

nodes = [0]
while len(nodes) != n :
    nodes.append(parent.index(nodes[-1]))

print(" -> ".join(map(str, nodes)))

borderTiles = set()
for i in range(0, n) :
    a, b = tiles[nodes[i - 1]], tiles[nodes[i]]
    if a[0] == b[0] :
        for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1) :
            borderTiles.add((a[0], y))
    else :
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1) :
            borderTiles.add((x, a[1]))

#print(borderTiles)
print(len(borderTiles))

tileY = [tile[1] for tile in tiles]
greenRangesY = {}
for y in range(min(tileY), max(tileY) + 1) :
    greenRangesY[y] = [border[0] for border in borderTiles if border[1] == y]
    greenRangesY[y].sort()


print(greenRangesY)
# areas = []
# for i in range(n) :
#     for j in range(i + 1, n) :
#         a, b = tiles[i], tiles[j]
#         # check if all borders are green
#         valid = True
#         for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1) :
            
#             if (x, a[1])(x, b[1]) :
#                 valid = False
#                 break
#         if not valid :
#             continue
#         for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1) :
#             if ((a[0], y) not in borderTiles) or ((b[0], y) not in borderTiles) :
#                 valid = False
#                 break
#         if not valid :
#             continue
#         areas.append([(abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1), i, j])

# areas.sort()
# print(areas[-1][0])

