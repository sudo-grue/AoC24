#!/usr/bin/env python3

from pathlib import Path

DEMO = "test.txt"
FULL = "data.txt"


def main():
    input_file = Path(__file__).parent / FULL

    # Parse as list of lists so points can be modified for part 2
    with input_file.open("r", encoding="ascii") as file:
        data = [list(line.strip()) for line in file.readlines()]

    # Using next against generator to discover starting point
    location = next(
        (row, col)
        for row, line in enumerate(data)
        for col, letter in enumerate(line)
        if letter == "^"
    )

    # Stash starting point for part 2
    # Gather all potential locations which are feasable for part 2
    start = location
    visited = set()

    turns = 0
    # North, East, South, West since guard can only turn right
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Store concrete values to avoid multiple calls to len() later
    dir_len = len(directions)
    rows = len(data)
    cols = len(data[0])

    # While guard is still within boundry
    while (0 <= location[0] < rows) and (0 <= location[1] < cols):
        visited.add(location)
        next_row = location[0] + directions[turns][0]
        next_col = location[1] + directions[turns][1]

        # While guard about to walk into a wall, turn right
        try:
            while data[next_row][next_col] == "#":
                turns += 1
                turns %= dir_len
                next_row = location[0] + directions[turns][0]
                next_col = location[1] + directions[turns][1]
        except IndexError:
            break

        location = (next_row, next_col)

    print(len(visited))

    # Remove starting point from potential locations
    visited.remove(start)
    loops = 0
    from_to = {}  # dict to track if we've traveled in the same direction

    for tgt_row, tgt_col in visited:
        # Place artifical wall to check for loop
        data[tgt_row][tgt_col] = "#"

        turns = 0
        location = start
        from_to.clear()

        while (0 <= location[0] < rows) and (0 <= location[1] < cols):
            next_row = location[0] + directions[turns][0]
            next_col = location[1] + directions[turns][1]

            try:
                while data[next_row][next_col] == "#":
                    turns += 1
                    turns %= dir_len
                    next_row = location[0] + directions[turns][0]
                    next_col = location[1] + directions[turns][1]
            except IndexError:
                break

            next_location = (next_row, next_col)

            been_next = from_to.get(location, set())
            if next_location in been_next:
                loops += 1
                break

            been_next.add(next_location)
            from_to[location] = been_next
            location = next_location

        # Clean up artifical wall for next attempt
        data[tgt_row][tgt_col] = "."

    print(loops)


if __name__ == "__main__":
    main()
