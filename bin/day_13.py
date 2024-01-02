from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


def find_reflections(pattern: list[list[str]]):
    reflections = []
    for i in range(len(pattern) - 1):
        # check if i><i+1 is reflection
        is_reflection = True
        limit = min(i + 1, len(pattern) - i - 1)
        for j in range(limit):
            if pattern[i - j] != pattern[i + 1 + j]:
                is_reflection = False
                break

        if is_reflection:
            reflections.append(i + 1)  # number of cols above line

    return reflections


def find_smudge_reflections(pattern: list[list[int]]):
    reflections = []
    for i in range(len(pattern) - 1):
        # check if i><i+1 is reflection
        limit = min(i + 1, len(pattern) - i - 1)
        total_diff = 0
        for j in range(limit):
            total_diff += sum(
                map(lambda a: abs(a[0] - a[1]), zip(pattern[i - j], pattern[i + 1 + j]))
            )

        if total_diff == 1:  # exactly one smudge
            reflections.append(i + 1)  # number of cols above line

    return reflections


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)

    h_reflections = 0
    v_reflections = 0
    pattern = []
    for line in lines:
        if line == "":
            # do work here
            h_ref = find_reflections(pattern)
            # transpose
            trans_pattern = list(map(list, zip(*pattern)))
            v_ref = find_reflections(trans_pattern)
            h_reflections += sum(h_ref)
            v_reflections += sum(v_ref)
            pattern = []
            continue

        pattern.append(list(line))

    # do work for final pattern here
    h_ref = find_reflections(pattern)
    # transpose
    trans_pattern = list(map(list, zip(*pattern)))
    v_ref = find_reflections(trans_pattern)
    h_reflections += sum(h_ref)
    v_reflections += sum(v_ref)

    return 100 * h_reflections + v_reflections


@time_it
def part_two(input_file: str):
    lines = load_and_split_lines(input_file)

    h_reflections = 0
    v_reflections = 0
    pattern = []
    for line in lines:
        if line == "":
            # do work here
            h_ref = find_smudge_reflections(pattern)
            # transpose
            trans_pattern = list(map(list, zip(*pattern)))
            v_ref = find_smudge_reflections(trans_pattern)
            h_reflections += sum(h_ref)
            v_reflections += sum(v_ref)
            pattern = []
            continue

        pattern.append([int(c == "#") for c in line])

    # do work for final pattern here
    h_ref = find_smudge_reflections(pattern)
    # transpose
    trans_pattern = list(map(list, zip(*pattern)))
    v_ref = find_smudge_reflections(trans_pattern)
    h_reflections += sum(h_ref)
    v_reflections += sum(v_ref)

    return 100 * h_reflections + v_reflections


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
