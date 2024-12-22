#!/usr/bin/python3
from collections import deque 

f = open("input.txt")
n = 16777216

s = 0
seqs = {}
for line in f :
	line = int(line[:-1])
	price = line % 10
	changes = []
	prices = []
	for i in range(2000) :
		line = ((line * 64) ^ line) % n
		line = ((line // 32) ^ line) % n
		line = ((line * 2048) ^ line) % n
		new_price = line % 10
		changes.append(str(new_price - price))
		price = new_price
		prices.append(price)
	
	current_seqs = {}
	for i in range(3, len(changes)) :
		seq = ''.join(changes[i - 3 : i + 1])
		if seq not in current_seqs :
			current_seqs[seq] = prices[i]

	for k in current_seqs.keys() :
		if k not in seqs :
			seqs[k] = current_seqs[k]
		else :
			seqs[k] += current_seqs[k]
	s += line

maxBananas = 0
for k, v in seqs.items() :
	if v > maxBananas :
		maxBananas = v

print(maxBananas)
