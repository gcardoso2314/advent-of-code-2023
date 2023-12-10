from math import lcm
from itertools import product

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@time_it
def part_one(input_file: str):
    lines = list(load_and_split_lines(input_file))
    instructions = lines[0]

    directions = {}
    for line in lines[2:]:
        start, ends = line.split(" = ")
        directions[start] = ends.strip("()").split(", ")

    location = "AAA"
    i = 0
    while location != "ZZZ":
        instr = instructions[i % len(instructions)]
        idx = int(instr == "R")
        location = directions[location][idx]
        i += 1

    return i


@time_it
def part_two(input_file: str):
    lines = list(load_and_split_lines(input_file))
    instructions = lines[0]

    directions = {}
    for line in lines[2:]:
        start, ends = line.split(" = ")
        directions[start] = ends.strip("()").split(", ")

    locations = [loc for loc in directions if loc.endswith("A")]
    end_points = []
    for loc in locations:
        i = 0
        visited = [(loc, i)]
        while True:
            instr = instructions[i % len(instructions)]
            idx = int(instr == "R")
            loc = directions[loc][idx]
            i += 1
            if (loc, i % len(instructions)) in visited:
                # hit a cycle
                break
            visited.append((loc, i))
        end_points.append([v for v in visited if v[0].endswith("Z")])

    return min([lcm(*[x[1] for x in comb]) for comb in product(*end_points)])


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
