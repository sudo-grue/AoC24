#!/usr/bin/env python3
"""
AoC24 Day 02 Part 1

The unusual data (your puzzle input) consists of many reports, one report per line.
Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety
systems can only tolerate levels that are either gradually increasing or gradually decreasing.
So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""

from pathlib import Path

DEMO = "example.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    reports = []
    with input_file.open("r", encoding="ascii") as file:
        reports = [list(map(int, line.split())) for line in file.readlines()]

    safe_reports = 0
    for report in reports:
        if safe(report):
            safe_reports += 1

    print(safe_reports)


def safe(report):
    if (report != sorted(report)) and (report != sorted(report, reverse=True)):
        return False

    return all(0 < abs(val - nxt) < 4 for val, nxt in zip(report, report[1:]))


if __name__ == "__main__":
    main()
