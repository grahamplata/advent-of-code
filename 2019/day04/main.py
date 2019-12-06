#!/usr/bin/env python3


"""Day04
Day 4 of Advent of Code
"""

import argparse
from collections import Counter


def runner(file_input):
    """runner
    """

    with open(file_input) as file:
        line = file.readline().strip().split('-')
        min_val, max_val = [int(i) for i in line]

    password_count_1 = 0
    password_count_2 = 0

    # The value is within the range given in your puzzle input.
    for value in range(min_val, max_val):
        string_val = str(value)

        # length must be 6
        if len(string_val) != 6:
            continue

        # Going from left to right, the digits never decrease;
        if ''.join(sorted(string_val)) != string_val:
            continue

        # Two adjacent digits are the same (like 22 in 122345).
        counter = Counter(string_val)
        (val, count), = counter.most_common(1)
        if count == 1:
            continue
        password_count_1 += 1

        #  Are not part of a larger group of matching digits
        if 2 not in counter.values():
            continue
        password_count_2 += 1

    print(f"Part 1: {password_count_1}")
    print(f"Part 2: {password_count_2}")


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
