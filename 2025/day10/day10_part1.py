#!/usr/bin/python3

f = open('input.txt')

get_state_key = lambda state : ''.join(['1' if light else '0' for light in state])
s = 0
for line in f :
    line = line[:-1].split()
    wanted_state = get_state_key([True if light == '#' else False for light in line[0][1:-1]])
    buttons = [list(map(int, button[1:-1].split(','))) for button in line[1:-1]]
    saved_states = {}
    states = [([False for _ in wanted_state], 0)]
    while wanted_state not in saved_states.keys() :
        state = states.pop(0)
        state_key = get_state_key(state[0])
        if state_key in saved_states.keys() :
            continue
        saved_states[state_key] = state[1]
        for button in buttons :
            new_state = [not state[0][i] if i in button else state[0][i] for i in range(len(state[0]))]
            states.append([new_state, state[1] + 1])
    s += saved_states[wanted_state]

print(s)