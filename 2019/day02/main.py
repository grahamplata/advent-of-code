#!/usr/bin/env python3

"""Day02
Day 2 of Advent of Code

Opcode 99 means that the program is finished and should immediately halt.
Opcode  1 adds numbers read from two positions and stores the result in a third position.
Opcode  2 multiplies numbers read from two positions and stores the result in a third position.

The three integers immediately after the opcode tell you these three positions
Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
"""

import argparse


def runner(program):
    """part_one
    """
    position = 0
    while True:
        opcode = program[position]
        if opcode == 99:
            return program[0]
        elif opcode == 1:
            program[program[position + 3]
                    ] = program[program[position + 2]] + program[program[position + 1]]
        elif opcode == 2:
            program[program[position + 3]
                    ] = program[program[position + 2]] * program[program[position + 1]]
        else:
            print("I am Broken...")
        position += 4
    return program[position]


def part_one(file_input):
    """part_one
    """
    program = [int(piece) for piece in file_input.strip().split(',')]
    program[1] = 12
    program[2] = 2
    return runner(program)


def part_two(file_input):
    """part_two
    """
    program = [int(piece) for piece in file_input.strip().split(',')]
    for noun in range(100):
        for verb in range(100):
            program_temp = program[:]
            program_temp[1] = noun
            program_temp[2] = verb
            if runner(program=program_temp) == 19690720:
                return 100 * noun + verb


def main():
    """main
    Main function

    Run with: python main.py --file input.txt
    """
    parser = argparse.ArgumentParser(
        description="Run Advent of code with input.")
    parser.add_argument("--file", required=True, help='Path to input file.')
    args = parser.parse_args()

    with open(args.file) as file:
        print(f"Part 1: {part_one(file_input=file.read())}")

    with open(args.file) as file:
        print(f"Part 2: {part_two(file_input=file.read())}")

    return


if __name__ == '__main__':
    exit(main())
