import re
from itertools import chain, repeat

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@time_it
def part_one(input_file: str):
    lines = list(load_and_split_lines(input_file))
    numbers_in_lines = [
        zip(repeat(i), re.finditer("\d+", line)) for i, line in enumerate(lines)
    ]

    total = 0
    for line_num, number in chain(*numbers_in_lines):
        top_line = max(0, line_num - 1)
        bot_line = min(len(lines) - 1, line_num + 1)
        left_index, right_index = number.span()
        left = max(0, left_index - 1)
        for i in range(top_line, bot_line + 1):
            if re.search(r"[^.0-9]", lines[i][left : right_index + 1]):
                total += int(number.group())
                break

    return total


@time_it
def part_two(input_file: str):
    lines = list(load_and_split_lines(input_file))
    stars_in_lines = [
        zip(repeat(i), re.finditer("\*", line)) for i, line in enumerate(lines)
    ]
    numbers_in_lines = [list(re.finditer("\d+", line)) for line in lines]

    total = 0
    for line_num, star in chain(*stars_in_lines):
        top_line = max(0, line_num - 1)
        bot_line = min(len(lines) - 1, line_num + 1)
        star_pos = star.span()[0]
        adjacent_nums = []
        for i in range(top_line, bot_line + 1):
            adjacent_nums.extend(
                [
                    num
                    for num in numbers_in_lines[i]
                    if num.span()[0] - 1 <= star_pos <= num.span()[1]
                ]
            )
        if len(adjacent_nums) == 2:
            total += int(adjacent_nums[0].group()) * int(adjacent_nums[1].group())

    return total


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
