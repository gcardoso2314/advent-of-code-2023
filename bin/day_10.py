from enum import Enum
from dataclasses import dataclass

from advent_of_code_2023.io import load_and_split_lines, parse_args
from advent_of_code_2023.time import time_it


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"


def shift_coordinate(
    coordinates: tuple[int, int], direction: Direction
) -> tuple[int, int]:
    if direction == Direction.NORTH:
        return coordinates[0] - 1, coordinates[1]
    elif direction == Direction.EAST:
        return coordinates[0], coordinates[1] + 1
    elif direction == Direction.WEST:
        return coordinates[0], coordinates[1] - 1
    elif direction == Direction.SOUTH:
        return coordinates[0] + 1, coordinates[1]


def opposite_direction(direction: Direction):
    if direction == Direction.NORTH:
        return Direction.SOUTH
    elif direction == Direction.EAST:
        return Direction.WEST
    elif direction == Direction.WEST:
        return Direction.EAST
    elif direction == Direction.SOUTH:
        return Direction.NORTH


@dataclass
class Pipe:
    connection: tuple[Direction, Direction]

    def move(self, entry_direction, coordinates):
        exit_direction = self.exit_direction(entry_direction)
        return shift_coordinate(coordinates, exit_direction)

    def exit_direction(self, entry_direction):
        return [conn for conn in self.connection if conn != entry_direction][0]


PIPES = {
    "|": Pipe((Direction.SOUTH, Direction.NORTH)),
    "-": Pipe((Direction.WEST, Direction.EAST)),
    "L": Pipe((Direction.NORTH, Direction.EAST)),
    "J": Pipe((Direction.NORTH, Direction.WEST)),
    "7": Pipe((Direction.SOUTH, Direction.WEST)),
    "F": Pipe((Direction.SOUTH, Direction.EAST)),
}


@time_it
def part_one(input_file: str):
    map = [list(line) for line in list(load_and_split_lines(input_file))]
    starting_point = [
        (i, line.index("S")) for i, line in enumerate(map) if "S" in line
    ][0]

    i = 0
    current_point = starting_point
    entry_direction = None
    while current_point != starting_point or i == 0:
        if i == 0:
            # try to find which way to go
            if (
                current_point[0] > 0
                and map[current_point[0] - 1][current_point[1]] in PIPES
                and Direction.SOUTH
                in PIPES[map[current_point[0] - 1][current_point[1]]].connection
            ):
                current_point = (current_point[0] - 1, current_point[1])
                entry_direction = Direction.SOUTH
            elif (
                current_point[1] > 0
                and map[current_point[0]][current_point[1] - 1] in PIPES
                and Direction.EAST
                in PIPES[map[current_point[0]][current_point[1] - 1]].connection
            ):
                current_point = (current_point[0], current_point[1] - 1)
                entry_direction = Direction.EAST
            elif (
                current_point[0] < len(map) - 1
                and map[current_point[0] + 1][current_point[1]] in PIPES
                and Direction.NORTH
                in PIPES[map[current_point[0] + 1][current_point[1]]].connection
            ):
                current_point = (current_point[0] + 1, current_point[1])
                entry_direction = Direction.NORTH
            elif (
                current_point[1] < len(map[0]) - 1
                and map[current_point[0]][current_point[1] + 1] in PIPES
                and Direction.WEST
                in PIPES[map[current_point[0]][current_point[1] + 1]].connection
            ):
                current_point = (current_point[0], current_point[1] + 1)
                entry_direction = Direction.WEST
            i += 1
        else:
            pipe = PIPES[map[current_point[0]][current_point[1]]]
            current_point = pipe.move(entry_direction, current_point)
            entry_direction = opposite_direction(pipe.exit_direction(entry_direction))
            i += 1

    return i / 2


@time_it
def part_two(input_file: str):
    pass


def main():
    args = parse_args()
    print(f"Result for part one is: {part_one(args.input_file)}")
    print(f"Result for part two is: {part_two(args.input_file)}")


if __name__ == "__main__":
    main()
