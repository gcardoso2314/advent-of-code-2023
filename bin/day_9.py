from operator import sub
from functools import reduce

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)

    total = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        seqs = [nums]
        while True:
            seq = list(map(sub, seqs[-1][1:], seqs[-1][:-1]))
            if not any(seq):
                break
            seqs.append(seq)

        total += sum([seq[-1] for seq in seqs])

    return total


@time_it
def part_two(input_file: str):
    lines = load_and_split_lines(input_file)

    total = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        seqs = [nums]
        while True:
            seq = list(map(sub, seqs[-1][1:], seqs[-1][:-1]))
            if not any(seq):
                break
            seqs.append(seq)

        first_numbers = [seq[0] for seq in seqs]
        total += reduce(lambda a, b: b - a, reversed(first_numbers))

    return total


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
