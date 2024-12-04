#!/usr/bin/env python3
"""
Looking for the instructions, you flip over the word search to find that this isn't
actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS
in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X,
each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again.
How many times does an X-MAS appear?
"""

from pathlib import Path

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    with input_file.open("r", encoding="ascii") as file:
        data = [line.strip() for line in file]

    total = 0
    for row in range(1, len(data) - 1):  # skip first/last rows
        for col in range(1, len(data[row]) - 1):  # skip first/last columns
            if "A" == data[row][col]:
                total += check_for_x(col, row, data)

    print(total)


def check_for_x(x, y, matrix):
    # Generate set for each portion of cross, removing the concern for ordering
    nw_se = {matrix[y - 1][x - 1], matrix[y + 1][x + 1]}
    ne_sw = {matrix[y - 1][x + 1], matrix[y + 1][x - 1]}

    target_set = {"M", "S"}
    if target_set == nw_se and target_set == ne_sw:
        return 1
    return 0


if __name__ == "__main__":
    main()
