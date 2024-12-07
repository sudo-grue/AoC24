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
        combination_count = 3 ** gap_count  # 3 for mask of three operations

        for int_mask in range(combination_count):
            calc_result = numbers[0]

            # can't create bitwise mask for 3 operations but
            # same logic can be applied with whole numbers
            # and destructive copies of an integer
            temp_mask = int_mask
            for i in range(gap_count):
                op_code = temp_mask % 3
                temp_mask //= 3

                match op_code:
                    case 0:
                        calc_result += numbers[i + 1]
                    case 1:
                        calc_result *= numbers[i + 1]
                    case 2:
                        calc_result = int(f"{calc_result}{numbers[i + 1]}")

            if calc_result == answer:
                total += calc_result
                break

    print(total)


if __name__ == "__main__":
    main()
