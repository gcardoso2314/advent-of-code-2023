from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@time_it
def part_one(input_file: str):
    almanac = list(load_and_split_lines(input_file))
    seed_nums = almanac[0].split(":")[1]
    seeds = [int(num) for num in seed_nums.split()]

    mappings: dict[str, str] = {}  # to save what maps to what e.g. seed to soil
    num_mappings: dict[
        str, dict[tuple[int, int], int]
    ] = {}  # saving the actual mappings

    current_source = ""
    current_destination = ""
    for line in almanac[1:]:
        if not line:
            continue

        if "map" in line:
            mapping = line.split()[0].split("-")
            current_source = mapping[0]
            current_destination = mapping[-1]
            mappings[current_source] = current_destination
            num_mappings[current_source] = {}
            continue

        destination_start, source_start, range_length = [
            int(num) for num in line.split()
        ]
        num_mappings[current_source].update(
            {(source_start, source_start + range_length): destination_start}
        )

    source = "seed"
    mapped_nums = seeds
    while source in mappings:
        next_nums = []
        for i, num in enumerate(mapped_nums):
            next_nums.append(num)
            for (source_start, source_end), destination_start in num_mappings[
                source
            ].items():
                if source_start <= num < source_end:
                    next_nums[i] = (num - source_start) + destination_start
                    break

        mapped_nums = next_nums
        source = mappings[source]

    return min(mapped_nums)


@time_it
def part_two(input_file: str):
    pass


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
