#!/usr/bin/python3

f = open("input.txt")
n = 16777216

s = 0
for line in f :
	line = int(line[:-1])
	#print(line)
	for i in range(2000) :
		line = ((line * 64) ^ line) % n
		#print(line)
		line = ((line // 32) ^ line) % n
		line = ((line * 2048) ^ line) % n
	s += line

print(s)