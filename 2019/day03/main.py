#!/usr/bin/env python3

"""Day03
Day 3 of Advent of Code
"""

import argparse

GRID_DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def runner(file_input):
    """runner
    """

    with open(file_input) as file:
        lines = [line.strip().split(',') for line in file]

    wire1 = [(val[0], int(val[1:])) for val in lines[0]]
    wire2 = [(val[0], int(val[1:])) for val in lines[1]]

    first_coordinate_set = set()
    first_steps = {}
    x1 = 0
    y1 = 0
    steps = 0

    for (direction, units) in wire1:
        x_direction, y_direction = GRID_DIRECTIONS[direction]
        for unit in range(units):
            x1 += x_direction
            y1 += y_direction
            steps += 1
            # print(f"X coordinate: {x1}, Y coordinate: {y1}, Current Step: {steps}")
            first_steps[(x1, y1)] = steps
            first_coordinate_set.add((x1, y1))

    intersections = set()
    x2 = 0
    y2 = 0
    steps2 = 0

    for (direction, units) in wire2:
        x_direction, y_direction = GRID_DIRECTIONS[direction]
        for unit in range(units):
            x2 += x_direction
            y2 += y_direction
            steps2 += 1
            if (x2, y2) in first_coordinate_set:
                intersections.add((x2, y2, steps2 + first_steps[(x2, y2)]))

    min_dist = min(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
    print(f"Part 1: {min_dist}")

    min_steps = min(map(lambda x: x[2], intersections))
    print(f"Part 2: {min_steps}")


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
