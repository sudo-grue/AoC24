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
        for combo in combinations(nodes[symbol], 2):
            x1, y1 = combo[0]
            x2, y2 = combo[1]
            diff_x = x2 - x1
            diff_y = y2 - y1

            # add the two candidates to solution if in bounds
            for loc in [(x1 - diff_x, y1 - diff_y), (x2 + diff_x, y2 + diff_y)]:
                if 0 <= loc[0] < rows and 0 <= loc[1] < cols:
                    solution.add(loc)

    print(len(solution))


if __name__ == "__main__":
    main()
