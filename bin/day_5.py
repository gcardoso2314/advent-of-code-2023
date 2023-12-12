from dataclasses import dataclass

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


@dataclass
class Mapping:
    source: str
    destination: str
    mapping_ranges: list[tuple[int, int, int]]


def map_range(
    pair: tuple[int, int], mapping_ranges: list[tuple[int, int, int]]
) -> set[tuple[int, int]]:
    output = set()
    pairs_to_map = set([pair])
    while pairs_to_map:
        next_pair = pairs_to_map.pop()
        any_overlap = False
        for mapping in mapping_ranges:
            if pair[0] <= mapping[1] and mapping[0] <= pair[1]:
                any_overlap = True
                start_overlap = max(pair[0], mapping[0])
                end_overlap = min(pair[1], mapping[1])
                output.add((start_overlap + mapping[2], end_overlap + mapping[2]))

                if start_overlap > pair[0]:
                    pairs_to_map.add((pair[0], start_overlap - 1))

                if end_overlap < pair[1]:
                    pairs_to_map.add((end_overlap + 1, pair[1]))

        if not any_overlap:
            # this pair needs to be mapped to itself
            output.add(pair)

    return output


@time_it
def part_one(input_file: str):
    almanac = list(load_and_split_lines(input_file))
    seed_nums = almanac[0].split(":")[1]
    seeds = [int(num) for num in seed_nums.split()]

    mappings: dict[str, Mapping] = {}

    current_source = ""
    current_destination = ""
    for line in almanac[1:]:
        if not line:
            continue

        if "map" in line:
            mapping = line.split()[0].split("-")
            current_source = mapping[0]
            current_destination = mapping[-1]
            mappings[current_source] = Mapping(
                source=current_source,
                destination=current_destination,
                mapping_ranges=[],
            )
            continue

        destination_start, source_start, range_length = [
            int(num) for num in line.split()
        ]
        mappings[current_source].mapping_ranges.append(
            (
                source_start,
                source_start + range_length,
                destination_start - source_start,
            )
        )

    source = "seed"
    mapped_nums = seeds
    while source in mappings:
        next_nums = []
        for i, num in enumerate(mapped_nums):
            next_nums.append(num)
            for source_start, source_end, offset in mappings[source].mapping_ranges:
                if source_start <= num < source_end:
                    next_nums[i] = num + offset
                    break

        mapped_nums = next_nums
        source = mappings[source].destination

    return min(mapped_nums)


@time_it
def part_two(input_file: str):
    almanac = list(load_and_split_lines(input_file))
    seed_nums = almanac[0].split(":")[1].split()
    seed_num_pairs = [
        (int(a), int(a) + int(b) - 1) for a, b in zip(seed_nums[::2], seed_nums[1::2])
    ]

    mappings: dict[str, Mapping] = {}
    current_source = ""
    for line in almanac[1:]:
        if not line:
            continue

        if "map" in line:
            mapping = line.split()[0].split("-")
            current_source = mapping[0]
            current_destination = mapping[-1]
            mappings[current_source] = Mapping(
                source=current_source,
                destination=current_destination,
                mapping_ranges=[],
            )
            continue

        destination_start, source_start, range_length = [
            int(num) for num in line.split()
        ]
        mappings[current_source].mapping_ranges.append(
            (
                source_start,
                source_start + range_length - 1,
                destination_start - source_start,
            )
        )

    min_location = None
    for seed_pair in seed_num_pairs:
        source = "seed"
        pairs_to_map = set([seed_pair])
        next_pairs = set()
        while source in mappings:
            mapping_ranges = mappings[source].mapping_ranges
            # map each pair to the next destination
            while pairs_to_map:
                pair = pairs_to_map.pop()
                any_overlap = False
                for mapping in mapping_ranges:
                    if pair[0] <= mapping[1] and mapping[0] <= pair[1]:
                        any_overlap = True
                        start_overlap = max(pair[0], mapping[0])
                        end_overlap = min(pair[1], mapping[1])
                        next_pairs.add(
                            (start_overlap + mapping[2], end_overlap + mapping[2])
                        )

                        if start_overlap > pair[0]:
                            pairs_to_map.add((pair[0], start_overlap - 1))

                        if end_overlap < pair[1]:
                            pairs_to_map.add((end_overlap + 1, pair[1]))

                if not any_overlap:
                    # this pair needs to be mapped to itself
                    next_pairs.add(pair)

            pairs_to_map = next_pairs
            next_pairs = set()
            source = mappings[source].destination

        if min_location:
            min_location = min(min([x[0] for x in pairs_to_map]), min_location)
        else:
            min_location = min([x[0] for x in pairs_to_map])

    return min_location


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
