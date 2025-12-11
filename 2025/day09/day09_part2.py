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

visited = [False for _ in range(n)] 
parent = [-1 for _ in range(n)]

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

# nodes = list of tiles index order by the shape made of green and red tiles.
nodes = [0]
while len(nodes) != n :
    nodes.append(parent.index(nodes[-1]))


# borderTiles = list of all points of the border of the shape
borderTiles = set()
for i in range(0, n) :
    a, b = tiles[nodes[i - 1]], tiles[nodes[i]]
    if a[0] == b[0] :
        for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1) :
            borderTiles.add((a[0], y))
    else :
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1) :
            borderTiles.add((x, a[1]))

minX, maxX = min([border[0] for border in borderTiles]), max([border[0] for border in borderTiles])
minY, maxY = min([border[1] for border in borderTiles]), max([border[1] for border in borderTiles]) 


## Ray Casting algorithm
## return True if is_inside the shape
def is_inside(p) :
    global borderTiles, minX, maxX, minY, maxY
    if p in borderTiles :
        return True
    if p[0] < minX or p[0] > maxX or p[1] < minY or p[1] > maxY :
        return False
    
    d_to_minX, d_to_maxX = p[0] - minX, maxX - p[0]
    d_to_minY, d_to_maxY = p[1] - minY, maxY - p[1]
    d_to_closest_border = min(d_to_minX, d_to_maxX, d_to_minY, d_to_maxY)
    
    nb_border = 0

    if d_to_closest_border == d_to_minX :
        current_x = p[0]
        while current_x >= minX :
            current_x -= 1
            if (current_x, p[1]) in borderTiles :
                nb_border += 1
                current_x -= 1
                while (current_x, p[1]) in borderTiles :
                    current_x -= 1
    elif d_to_closest_border == d_to_maxX :
        current_x = p[0]
        while current_x <= maxX :
            current_x += 1
            if (current_x, p[1]) in borderTiles :
                nb_border += 1
                current_x += 1
                while (current_x, p[1]) in borderTiles :
                    current_x += 1
    elif d_to_closest_border == d_to_minY :
        current_y = p[1]
        while current_y >= minY :
            current_y -= 1
            if (p[0], current_y) in borderTiles :
                nb_border += 1
                current_y -= 1
                while (p[0], current_y) in borderTiles :
                    current_y -= 1
    else :
        current_y = p[1]
        while current_y <= maxY :
            current_y += 1
            if (p[0], current_y) in borderTiles :
                nb_border += 1
                current_y += 1
                while (p[0], current_y) in borderTiles :
                    current_y += 1
    
    return (nb_border % 2) == 1     


areas = []
for i in range(n) :
    for j in range(i + 1, n) :
        a, b = tiles[i], tiles[j]
        areas.append([(abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1), i, j])

areas.sort(reverse=True)

# Find the first area with all borders inside the shape
for area in areas :
    a, b = tiles[area[1]], tiles[area[2]]

    borders = set()
    for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1) :
        borders.add((a[0], y))
        borders.add((b[0], y))
    for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1) :
        borders.add((x, a[1]))
        borders.add((x, b[1]))

    valid = True
    for border in borders :
        if not is_inside(border) :
            valid = False
            break
    if valid :
        print(area[0])
        break
