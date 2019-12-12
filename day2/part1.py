# Advent of Code - Day 2, Part 1

import operator

# code for the intcode program - includes specified variation to restore the gravity assist program to the "1202 program alarm" state it had just before the last computer caught fire
intcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0]

# test samples
test1 = [1,0,0,0,99] # --> [2,0,0,0,99]
test2 = [2,3,0,3,99] # --> [2,3,0,6,99]
test3 = [2,4,4,5,99,0] # --> [2,4,4,5,99,9801]
test4 = [1,1,1,4,99,5,6,0,99] # --> [30,1,1,4,2,5,6,0,99]

def program(intcode):
  """accepts list of integers, runs while loop with counter to move four indices at a time, checks value at zeroth position to determine opcode, extracts positions based on values from the following three positions, runs operation based on values at first two new positions and stores total in the third; returns new list when complete, aka opcode equals 99"""
  i = 0
  ops = {"+": operator.add, "*": operator.mul}
  while i < len(intcode):
    if intcode[i] == 1:
      op = "+"
    elif intcode[i] == 2:
      op = "*"
    elif intcode[i] == 99:
      return intcode
    pos1 = intcode[i + 1]
    pos2 = intcode[i + 2]
    pos3 = intcode[i + 3]
    total = ops[op](intcode[pos1], intcode[pos2])
    intcode[pos3] = total
    i += 4


print(program(intcode))