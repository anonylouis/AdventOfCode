#!/usr/bin/python3

f = open('input.txt')

pts = {
  "A": 1,
  "B": 2,
  "C": 3
}

convert = {
	"X" :
	{
		"A": "C",
		"B": "A",
		"C": "B"
	},
	"Y" :
	{
		"A": "A",
		"B": "B",
		"C": "C"
	},
	"Z" :
	{
		"A": "B",
		"B": "C",
		"C": "A"
	}
}

score = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

s = 0
for l in f :
	player1, to_play = l[:-1].split(" ")
	s+=pts[convert[to_play][player1]]
	s+=score[to_play]

print(s)
