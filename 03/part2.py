#!/usr/bin/env python3
"""
There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of
the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time
the mul(5,5) and mul(11,8) instructions are disabled because there is
a don't() instruction before them. The other mul instructions function normally,
including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the
results of just the enabled multiplications?
"""

from pathlib import Path
import re

DEMO = "example.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    with input_file.open("r", encoding="ascii") as file:
        data = "".join(line.strip() for line in file)

    instructions_pattern = r"mul\((\d+),(\d+)\)"
    fields_pattern = r"(?:^|do\(\))(.*?)(?:(?:don't\(\))|$)"

    total = 0
    for field in re.findall(fields_pattern, data):
        for instruction in re.findall(instructions_pattern, field):
            total += int(instruction[0]) * int(instruction[1])

    print(total)


if __name__ == "__main__":
    main()
