from collections import Counter
from enum import Enum

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


class Direction(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3


def tilt(rocks: list[str], direction: Direction):
    # transpose to make it easier to work with rows rather than cols
    if direction == Direction.NORTH:
        transform_rocks = list(map("".join, zip(*rocks)))
    elif direction == Direction.EAST:
        transform_rocks = list(map(lambda x: x[::-1], rocks))
    elif direction == Direction.SOUTH:
        transform_rocks = list(map(lambda x: x[::-1], map("".join, zip(*rocks))))
    elif direction == Direction.WEST:
        transform_rocks = rocks.copy()

    tilted_rocks = []
    for row in transform_rocks:
        sections = row.split("#")
        tilted_result = []
        for section in sections:
            num_rocks = Counter(section)["O"]
            tilted_result.append("O" * num_rocks + "." * (len(section) - num_rocks))

        tilted_rocks.append("#".join(tilted_result))

    # transform back
    if direction == Direction.NORTH:
        return list(map("".join, zip(*tilted_rocks)))
    elif direction == Direction.EAST:
        return list(map(lambda x: x[::-1], tilted_rocks))
    elif direction == Direction.SOUTH:
        return list(map("".join, zip(*map(lambda x: x[::-1], tilted_rocks))))
    elif direction == Direction.WEST:
        return tilted_rocks


def calculate_load(rocks: list[str]):
    load = 0
    for i, row in enumerate(rocks):
        load += Counter(row)["O"] * (len(rocks) - i)

    return load


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)
    rocks = list(lines)
    tilted_rocks = tilt(rocks, Direction.NORTH)

    return calculate_load(tilted_rocks)


@time_it
def part_two(input_file: str):
    n_cycles = 1000000000
    lines = load_and_split_lines(input_file)
    rocks = list(lines)
    tilted_rocks = rocks.copy()
    cycle_results = []
    for _ in range(n_cycles):
        for direction in range(4):
            tilted_rocks = tilt(tilted_rocks, Direction(direction))

        if tilted_rocks in cycle_results:
            break

        cycle_results.append(tilted_rocks.copy())

    chain_start = cycle_results.index(tilted_rocks)
    final_result = (n_cycles - chain_start) % (len(cycle_results) - chain_start)

    return calculate_load(cycle_results[chain_start + final_result - 1])


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
