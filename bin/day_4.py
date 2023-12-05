from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


def parse_card(card: str):
    numbers = card.split(":")[1]
    winning_nums, our_nums = numbers.split("|")
    winning_nums = [num.strip() for num in winning_nums.split()]
    our_nums = [num.strip() for num in our_nums.split()]
    return winning_nums, our_nums


@time_it
def part_one(input_file: str):
    cards = load_and_split_lines(input_file)
    total = 0
    for card in cards:
        winning_nums, our_nums = parse_card(card)
        total_winning_numbers = len(set(winning_nums).intersection(set(our_nums)))
        total += 2 ** (total_winning_numbers - 1) if total_winning_numbers else 0

    return total


@time_it
def part_two(input_file: str):
    cards = list(load_and_split_lines(input_file))
    card_counts = [1] * len(cards)
    for i, card in enumerate(cards):
        winning_nums, our_nums = parse_card(card)
        total_winning_numbers = len(set(winning_nums).intersection(set(our_nums)))
        for j in range(i + 1, i + total_winning_numbers + 1):
            card_counts[j] += card_counts[i]

    return sum(card_counts)


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
