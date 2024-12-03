#!/usr/bin/env python3
"""
It seems like the goal of the program is just to multiply some numbers. It does
that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly,
mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many
invalid characters that should be ignored, even if they look like part of a mul
instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or
mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the
result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get
if you add up all of the results of the multiplications?
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

    total = 0
    for instruction in re.findall(instructions_pattern, data):
        total += int(instruction[0]) * int(instruction[1])

    print(total)


if __name__ == "__main__":
    main()
