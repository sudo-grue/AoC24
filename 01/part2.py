#!/usr/bin/env python3
"""
AoC24 Day 01 Part 2

This time, you'll need to figure out exactly how often each number from the left list appears in
the right list. Calculate a total similarity score by adding up each number in the left list after
multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.

The similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""

from pathlib import Path
from collections import Counter

DEMO = "example.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    lefts = []
    rights = []
    with input_file.open("r", encoding="ascii") as file:
        for line in file:
            left, right = line.split()
            lefts.append(int(left))
            rights.append(int(right))

    occurrences = Counter(rights)

    total = 0
    for num in lefts:
        total += num * occurrences[num]

    print(total)


if __name__ == "__main__":
    main()
