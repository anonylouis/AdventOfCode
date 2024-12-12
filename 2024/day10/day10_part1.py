#!/usr/bin/python3

f = open('input.txt')

M = []

for line in f :
    M.append(list(map(int, line[:-1])))

n, m = len(M), len(M[0])
score = 0 

for i in range(n) :
    for j in range(m) :
        if M[i][j] == 0 :
            final_trail = set()
            paths = [[i, j]]
            while len(paths) != 0 :
                path_i, path_j = paths.pop()
                path_value = M[path_i][path_j]
                if (path_value == 9) : 
                    final_trail.add((path_i, path_j))
                else :
                    if path_i > 0 and M[path_i - 1][path_j] == (path_value + 1) :
                        paths.append([path_i - 1, path_j])
                    if path_i < (n - 1) and M[path_i + 1][path_j] == (path_value + 1) :
                        paths.append([path_i + 1, path_j])
                    if path_j > 0 and M[path_i][path_j - 1] == (path_value + 1) :
                        paths.append([path_i, path_j - 1])
                    if path_j < (m - 1) and M[path_i][path_j + 1] == (path_value + 1) :
                        paths.append([path_i, path_j + 1])
            score += len(final_trail)

print(score)
