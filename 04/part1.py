#!/usr/bin/env python3
"""
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt;
she'd like to know if you could help her with her word search (your puzzle input). She only has
to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or
even overlapping other words. It's a little unusual, though, as you don't merely need to find
one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear,
where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again,
but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?
"""

from pathlib import Path

DEMO = "test.txt"
FULL = "data.txt"

TARGET = "XMAS"


def main():
    input_file = Path(__file__).parent / FULL

    with input_file.open("r", encoding="ascii") as file:
        data = [line.strip() for line in file]

    total = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == TARGET[0]:
                total += check(col, row, data)

    print(total)


def check(x, y, matrix):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total = 0
    for mod_y, mod_x in neighbors:
        # ensure direction of travel will not take us out-of-bounds
        limit_x = x + (3 * mod_x)
        limit_y = y + (3 * mod_y)
        if not ((0 <= limit_x < len(matrix[0])) and (0 <= limit_y < len(matrix))):
            continue

        # Check for full string match and increment only if loop finished successfully
        for idx, letter in enumerate(TARGET):
            new_y = (mod_y * idx) + y
            new_x = (mod_x * idx) + x
            if letter != matrix[new_y][new_x]:
                break
        else:
            total += 1

    return total


if __name__ == "__main__":
    main()
