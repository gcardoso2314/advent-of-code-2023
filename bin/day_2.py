import re
from argparse import ArgumentParser

from advent_of_code_2023.io import load_and_split_lines
from advent_of_code_2023.time import time_it

LIMITS = {"red": 12, "green": 13, "blue": 14}


def get_game_cube_counts(line: str):
    colour_pattern = r"(\d+) (blue|red|green)"
    game, sets = line.split(":")
    game_id = int(game.split()[-1])
    cube_counts = [(int(num), col) for num, col in re.findall(colour_pattern, sets)]

    return game_id, cube_counts


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)

    total = 0
    for line in lines:
        game_id, cube_counts = get_game_cube_counts(line)
        possible = True
        for num, col in cube_counts:
            if num > LIMITS[col]:
                possible = False
                break

        total += game_id * possible

    return total


@time_it
def part_two(input_file: str):
    lines = load_and_split_lines(input_file)

    total = 0
    for line in lines:
        max_needed = dict()
        _, cube_counts = get_game_cube_counts(line)
        sorted_counts = sorted(cube_counts, key=lambda x: x[0], reverse=True)
        for num, col in sorted_counts:
            if len(max_needed) == 3:
                # we have the max for each colour
                break

            if col not in max_needed:
                max_needed[col] = num

        total += max_needed["blue"] * max_needed["red"] * max_needed["green"]

    return total


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", type=str)
    args = parser.parse_args()
    print(f"Answer for part 1: {part_one(args.input_file)}")
    print(f"Answer for part 2: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
