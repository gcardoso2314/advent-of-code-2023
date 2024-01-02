import re
from functools import cache

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it

# if . - if end of block, check pattern number. skip
# if # - add count to current block
# if ? - split into two branches


@cache
def count_pos(parts, pattern, current_block_length):
    if len(parts) == 0:
        if len(pattern) == 0:
            return 1
        elif len(pattern) == 1 and current_block_length == pattern[0]:
            return 1
        else:
            return 0

    if len(pattern) == 0:
        if re.search("#", parts):
            return 0
        else:
            return 1

    if parts[0] == ".":
        if current_block_length == 0:
            # regular old .
            return count_pos(parts[1:], pattern, 0)
        elif current_block_length > 0:
            if current_block_length != pattern[0]:
                return 0
            else:
                return count_pos(parts[1:], pattern[1:], 0)
    elif parts[0] == "#":
        return count_pos(parts[1:], pattern, current_block_length + 1)
    elif parts[0] == "?":
        return count_pos("." + parts[1:], pattern, current_block_length) + count_pos(
            "#" + parts[1:], pattern, current_block_length
        )


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)
    total = 0
    for line in lines:
        parts, pattern = line.split()
        pattern = tuple(int(x) for x in pattern.split(","))
        total += count_pos(parts, pattern, 0)

    return total


@time_it
def part_two(input_file: str):
    lines = load_and_split_lines(input_file)
    total = 0
    for line in lines:
        parts, pattern = line.split()
        parts = "?".join([parts] * 5)
        pattern = tuple(int(x) for x in pattern.split(",")) * 5
        total += count_pos(parts, pattern, 0)

    return total


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
