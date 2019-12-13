# Advent of Code - Day 2, Part 2

import operator

# code for the intcode program - the "noun" and "verb" have been replaced with "20" and "3" to ensure the "output" equals 19690720
intcode = [1,20,3,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0]


def program(intcode):
  """accepts intcode program, runs while loop with counter to move four addresses at a time, checks opcode at the instruction pointer, extracts addresses based on values from the instruction's parameters, runs operation based on the noun and the verb and stores total in the third paramter; returns new program when complete, aka opcode equals 99"""
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


# GLOSSARY:
# -----------------------------------------------------
# Intcode Programs - list of integers / initial state for the computer's memory
# Address - a position in memory; e.g. the 1st value is at "address 0" or intcode[0]
# Opcodes - mark the beginning of an instruction; e.g. 1, 2, 99
# Parameters - the values used immediately after an opcode
# Instruction Pointer - the address of the current instruction
# Noun - the value placed in address 1; e.g. intcode[1], intcode[5], etc.
# Verb - the value placed in address 2; e.g. intcode[2], intcode[6], etc.