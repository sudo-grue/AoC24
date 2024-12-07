#!/usr/bin/env python3

from pathlib import Path

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    # Parse as list of lists so points can be modified for part 2
    with input_file.open("r", encoding="ascii") as file:
        data = [line.strip().split(": ") for line in file.readlines()]

    total = 0
    for answer, raw_numbers in data:
        answer = int(answer)
        numbers = list(map(int, raw_numbers.split()))
        gap_count = len(numbers) - 1
        combination_count = 2 ** gap_count  # 2 for mask of two operations

        # Creates bitmask for all +/* possibilities
        for bit_mask in range(combination_count):
            calc_result = numbers[0]

            for i in range(gap_count):
                if (bit_mask >> i) & 1:
                    calc_result *= numbers[i + 1]
                else:
                    calc_result += numbers[i + 1]

            if calc_result == answer:
                total += calc_result
                break

    print(total)


if __name__ == "__main__":
    main()
