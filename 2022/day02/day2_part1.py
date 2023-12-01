#!/usr/bin/python3

f = open('input.txt')

pts = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

s = 0
for l in f :
	player1, player2 = l[:-1].split(" ")
	s+=pts[player2]
	if (player1 == "A" and player2=="Y") or (player1 == "B" and player2=="Z") or (player1 == "C" and player2=="X") :
		s += 6
	elif (player1 == "A" and player2=="X") or (player1 == "B" and player2=="Y") or (player1 == "C" and player2=="Z") :
		s+= 3

print(s)
