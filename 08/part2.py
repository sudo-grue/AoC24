#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict
from itertools import combinations

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    with input_file.open("r", encoding="ascii") as file:
        data = [list(line.strip()) for line in file.readlines()]

    nodes = defaultdict(set)
    for row, line in enumerate(data):
        for col, symbol in enumerate(line):
            if symbol != ".":
                nodes[symbol].add((row, col))

    rows = len(data)
    cols = len(data[0])
    solution = set()

    for symbol in nodes:
        for pair in combinations(nodes[symbol], 2):
            x1, y1 = pair[0]
            x2, y2 = pair[1]
            diff_x = x2 - x1
            diff_y = y2 - y1

            # direction of travel in relation to pair[0] and pair[1]
            # is very important, otherwise overlaping the other node
            # will not be achieved, and solution will be missing origin pairs
            solution.update(scan(x1, y1, diff_x, diff_y, rows, cols))
            solution.update(scan(x2, y2, -diff_x, -diff_y, rows, cols))

    print(len(solution))


def scan(x, y, step_x, step_y, rows, cols):
    locations = set()
    while True:
        x += step_x
        y += step_y

        if (0 <= x < rows) and (0 <= y < cols):
            locations.add((x, y))
        else:
            break

    return locations


if __name__ == "__main__":
    main()
