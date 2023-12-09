import math
import re

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@time_it
def part_one(input_file: str):
    time_input, distance_input = list(load_and_split_lines(input_file))
    times = time_input.split(":")[1].split()
    distances = distance_input.split(":")[1].split()

    n_times_to_beat = []
    for time, distance in zip(times, distances):
        total_time = int(time.strip())
        record_distance = int(distance.strip())
        sol_1 = -(-total_time + (total_time**2 - 4 * record_distance) ** 0.5) / 2
        sol_2 = -(-total_time - (total_time**2 - 4 * record_distance) ** 0.5) / 2
        n_times_to_beat.append(int(sol_2 - 0.001) - int(sol_1))

    return math.prod(n_times_to_beat)


@time_it
def part_two(input_file: str):
    time_input, distance_input = list(load_and_split_lines(input_file))
    times = time_input.split(":")[1]
    distances = distance_input.split(":")[1]

    total_time = int(re.sub(r"\s", "", times))
    record_distance = int(re.sub(r"\s", "", distances))
    sol_1 = -(-total_time + (total_time**2 - 4 * record_distance) ** 0.5) / 2
    sol_2 = -(-total_time - (total_time**2 - 4 * record_distance) ** 0.5) / 2
    return int(sol_2 - 0.001) - int(sol_1)


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
