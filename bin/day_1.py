import re
from time import time
from argparse import ArgumentParser

from advent_of_code_2023.io import load_and_split_lines

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

REVERSE_NUMBERS = {num[::-1]: val for num, val in NUMBERS.items()}


def scan_line(line: str, reverse: bool = False) -> str:
    """Scan line and return when a number is found (either spelled or digit)"""
    number_map = REVERSE_NUMBERS if reverse else NUMBERS
    line = line[::-1] if reverse else line

    for i, char in enumerate(line):
        if char in "123456789":
            return char

        for num in number_map:
            if num in line[i : i + 5]:
                return number_map[num]


def part_one(input_file: str):
    total = 0
    num_pattern = re.compile(r"\d")
    for line in load_and_split_lines(input_file):
        digits = re.findall(num_pattern, line)
        total += int(digits[0] + digits[-1])

    return total


def part_two(input_file: str):
    total = 0
    for line in load_and_split_lines(input_file):
        first = scan_line(line)
        last = scan_line(line, reverse=True)
        total += int(first + last)

    return total


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("--part", type=int, default=1)

    args = parser.parse_args()
    if args.part == 1:
        start = time()
        result = part_one(args.input_file)
        print(f"Function took: {time() - start}")
        print(result)
    elif args.part == 2:
        start = time()
        result = part_two(args.input_file)
        print(f"Function took: {time() - start}")
        print(result)
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
