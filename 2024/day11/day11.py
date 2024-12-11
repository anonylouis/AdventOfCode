#!/usr/bin/python3

# stones is a map of stone -> number of stone
stones = {}

for value in list(map(int, open('input.txt').readline().split())) :
	stones[value] = 1

def addValueToMap(_map, _key, _value) :
	if _key in _map :
		_map[_key] = _map[_key] + _value
	else :
		_map[_key] = _value

for i in range(75) :
	new_stones = {}
	for stone in stones :
		number = stones[stone]
		if stone == 0 :
			addValueToMap(new_stones, 1, number)
		else :
			str_stone = str(stone)
			str_len = len(str_stone)
			if str_len % 2 == 0 :
				addValueToMap(new_stones, int(str_stone[: str_len // 2]), number)
				addValueToMap(new_stones, int(str_stone[str_len // 2:]), number)
			else :
				addValueToMap(new_stones, stone * 2024, number)
	stones = new_stones
	if i == 24 or i == 74 :
		print(sum([stones[stone] for stone in stones]))
