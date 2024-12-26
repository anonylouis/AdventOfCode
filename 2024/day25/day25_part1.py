#!/usr/bin/python3

lines = open('input.txt').readlines()

locks = []
keys = []

for i in range(0, len(lines), 8) :
    if lines[i].startswith("#####") :
        lock = [0, 0, 0, 0, 0]
        for j in range(i + 1, i + 7) :
            for k in range(5) :
                if lines[j][k] == '#' :
                    lock[k] += 1
        locks.append(lock)
    else :
        key = [0, 0, 0, 0, 0]
        for j in range(i + 5, i - 1, -1) :
            for k in range(5) :
                if lines[j][k] == '#' :
                    key[k] += 1
        keys.append(key)

print(locks)
print(keys)

s = 0
for lock in locks :
    for key in keys :
        s += all([(lock[i] + key[i]) < 6 for i in range(5)])

print(s)