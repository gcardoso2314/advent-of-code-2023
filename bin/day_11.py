from functools import partial
from itertools import combinations

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


def expand_cosmos(cosmos: list[list[str]]):
    expanded_cosmos: list[list[str]] = []

    # handle rows
    for row in cosmos:
        expanded_cosmos.append(row.copy())
        if not "#" in row:
            expanded_cosmos.append(row.copy())

    # handle cols
    cols_duplicated = 0
    for i in range(len(cosmos[0])):
        col = [row[i] for row in cosmos]
        if not "#" in col:
            for row in expanded_cosmos:
                row.insert(i + cols_duplicated, ".")
            cols_duplicated += 1

    return expanded_cosmos


def find_expanded_rows_and_cols(cosmos: list[list[str]]):
    expanded_rows: set[int] = set()
    expanded_cols: set[int] = set()

    # handle rows
    for i, row in enumerate(cosmos):
        if not "#" in row:
            expanded_rows.add(i)

    # handle cols
    for i in range(len(cosmos[0])):
        col = [row[i] for row in cosmos]
        if not "#" in col:
            expanded_cols.add(i)

    return expanded_rows, expanded_cols


def find_galaxies(cosmos: list[list[str]]):
    galaxies = []
    for i, row in enumerate(cosmos):
        for j, point in enumerate(row):
            if point == "#":
                galaxies.append((i, j))
    return galaxies


def manhattan_distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


@time_it
def part_one(input_file: str):
    cosmos = [list(line) for line in load_and_split_lines(input_file)]
    expanded_rows, expanded_cols = find_expanded_rows_and_cols(cosmos)
    galaxies = find_galaxies(cosmos)
    galaxy_pairs = combinations(galaxies, r=2)

    total = 0
    for a, b in galaxy_pairs:
        total += manhattan_distance(a, b)
        min_row, max_row = sorted([a[0], b[0]])
        min_col, max_col = sorted([a[1], b[1]])
        rows_crossed = len(expanded_rows.intersection(range(min_row + 1, max_row)))
        cols_crossed = len(expanded_cols.intersection(range(min_col + 1, max_col)))
        total += rows_crossed + cols_crossed

    return total


@time_it
def part_two(input_file: str):
    cosmos = [list(line) for line in load_and_split_lines(input_file)]
    expanded_rows, expanded_cols = find_expanded_rows_and_cols(cosmos)
    galaxies = find_galaxies(cosmos)
    galaxy_pairs = combinations(galaxies, r=2)

    total = 0
    for a, b in galaxy_pairs:
        total += manhattan_distance(a, b)
        min_row, max_row = sorted([a[0], b[0]])
        min_col, max_col = sorted([a[1], b[1]])
        rows_crossed = len(expanded_rows.intersection(range(min_row + 1, max_row)))
        cols_crossed = len(expanded_cols.intersection(range(min_col + 1, max_col)))
        total += rows_crossed * 999_999 + cols_crossed * 999_999

    return total


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
