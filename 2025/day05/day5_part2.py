#!/usr/bin/python3

f = open('input.txt')

ranges = []
for line in f :
    if line == "\n" :
        break
    a, b = map(int, line[:-1].split('-'))
    ranges.append([a, b])

ranges.sort()

final_ranges = [ranges[0]]

for r in ranges[1:] :
    a, b = r
    if b <= final_ranges[-1][1] :
        # the range doesn't apprend any new values
        continue

    if a <= final_ranges[-1][1] :
        a = final_ranges[-1][1] + 1

    final_ranges.append([a, b])

print(sum([b - a + 1 for a, b in final_ranges]))
