#!/usr/bin/python3

instructions = open('input.txt').readline()[:-1]

print(instructions.count("(") - instructions.count(")"))
