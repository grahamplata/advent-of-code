#!/usr/bin/env python3

"""Day01
Day 1 of Advent of Code
"""

import argparse


def part_one(file_input):
    """part_one
    """
    total = 0
    for line in file_input.splitlines():
        total += int(line) // 3 - 2
    return total


def part_two(file_input):
    """part_two
    """
    total = 0
    for line in file_input.splitlines():
        previous_line = int(line)
        while previous_line > 0:
            previous_line = max(previous_line // 3 - 2, 0)
            total += previous_line
    return total


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
