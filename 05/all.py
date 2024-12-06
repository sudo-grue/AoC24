#!/usr/bin/env python3

from pathlib import Path

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    with input_file.open("r", encoding="ascii") as file:
        ordering, requests = file.read().split("\n\n")

    ordering = [tuple(map(int, rule.split("|"))) for rule in ordering.split()]
    requests = [list(map(int, request.split(","))) for request in requests.split()]

    graph = {}
    for before, after in ordering:
        graph[(before, after)] = -1
        graph[(after, before)] = 1

    part1 = 0
    part2 = 0
    for request in requests:
        # Craft a custom sort function for each specific set of data
        priority_func = calc_priority(graph, request)
        result = sorted(request, key=priority_func)

        if request == result:
            part1 += request[len(result) // 2]
        else:
            part2 += result[len(result) // 2]

    print(f"{part1 = }")
    print(f"{part2 = }")


def calc_priority(graph, request):
    def priority(x):
        return sum(graph.get((x, y), 0) for y in request)

    return priority


if __name__ == "__main__":
    main()
