from collections import Counter
from operator import itemgetter

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it

CARD_VALUES_PART_ONE = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
CARD_VALUES_PART_TWO = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
CARD_VALUES_PART_ONE.update({str(i): i for i in range(2, 10)})
CARD_VALUES_PART_TWO.update({str(i): i for i in range(2, 10)})


def create_hand_tuple_part_one(hand):
    # (most_common, num_unique, first, second, third, fourth, fifth)
    c = Counter(hand)
    return (
        c.most_common(1)[0][1],
        len(c),
        CARD_VALUES_PART_ONE[hand[0]],
        CARD_VALUES_PART_ONE[hand[1]],
        CARD_VALUES_PART_ONE[hand[2]],
        CARD_VALUES_PART_ONE[hand[3]],
        CARD_VALUES_PART_ONE[hand[4]],
    )


def create_hand_tuple_part_two(hand):
    # (most_common, num_unique, first, second, third, fourth, fifth)
    c = Counter(hand)
    top_2 = c.most_common(2)

    if len(c) == 1:
        most_common_ct = 5
        num_unique = 1
    elif top_2[0][0] == "J":
        most_common_ct = top_2[1][1] + c["J"]
        num_unique = len(c) - bool(c["J"])
    else:
        most_common_ct = top_2[0][1] + c["J"]
        num_unique = len(c) - bool(c["J"])

    return (
        most_common_ct,
        num_unique,
        CARD_VALUES_PART_TWO[hand[0]],
        CARD_VALUES_PART_TWO[hand[1]],
        CARD_VALUES_PART_TWO[hand[2]],
        CARD_VALUES_PART_TWO[hand[3]],
        CARD_VALUES_PART_TWO[hand[4]],
    )


def multisort(hands, specs):
    for key, reverse in reversed(specs):
        hands.sort(key=lambda x: x[0][key], reverse=reverse)
    return hands


@time_it
def part_one(input_file: str):
    lines = load_and_split_lines(input_file)
    hands = [line.split() for line in lines]
    hand_tuples = [(create_hand_tuple_part_one(hand), int(bid)) for hand, bid in hands]
    sorted_hands = multisort(
        hand_tuples,
        specs=(
            (0, False),
            (1, True),  # less unique cards is better
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, False),
        ),
    )

    return sum([hand[1] * (i + 1) for i, hand in enumerate(sorted_hands)])


@time_it
def part_two(input_file: str):
    lines = load_and_split_lines(input_file)
    hands = [line.split() for line in lines]
    hand_tuples = [(create_hand_tuple_part_two(hand), int(bid)) for hand, bid in hands]
    sorted_hands = multisort(
        hand_tuples,
        specs=(
            (0, False),
            (1, True),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, False),
        ),
    )

    return sum([hand[1] * (i + 1) for i, hand in enumerate(sorted_hands)])


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
