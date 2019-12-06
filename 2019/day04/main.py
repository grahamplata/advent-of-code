#!/usr/bin/env python3

"""Day04
Day 4 of Advent of Code

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""

import argparse


def runner(file_input):
    """runner
    """

    with open(file_input) as file:
        line = file.readline()
        values = line.split('-')
        min_val, max_val = [int(i) for i in values]

    for i in range(min_val, max_val):
        print(i)


def main():
    """main
    Main function

    Run with: python main.py --file input.txt
    """
    parser = argparse.ArgumentParser(
        description="Run Advent of code with input.")
    parser.add_argument("--file", required=True, help='Path to input file.')
    args = parser.parse_args()
    runner(file_input=args.file)

    return


if __name__ == '__main__':
    exit(main())
