#!/usr/bin/env python3
"""
AoC24 Day 02 Part 2

Now, the same rules apply as before, except if removing a single level from
an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can
remove a single level from unsafe reports. How many reports are now safe?
"""

from pathlib import Path
from itertools import combinations

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    reports = []
    with input_file.open("r", encoding="ascii") as file:
        reports = [list(map(int, line.split())) for line in file.readlines()]

    safe_reports = 0
    for report in reports:
        levels = len(report)

        full = safe(report)
        corrected = any(safe(list(seq)) for seq in combinations(report, levels - 1))

        if full or corrected:
            safe_reports += 1

    print(safe_reports)


def safe(report):
    if (report != sorted(report)) and (report != sorted(report, reverse=True)):
        return False

    return all(0 < abs(val - nxt) < 4 for val, nxt in zip(report, report[1:]))


if __name__ == "__main__":
    main()
