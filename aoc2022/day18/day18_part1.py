from typing import Set

from aoc2022.day18.day18_common import load_data, adjacent, Coord


def area(droplets: Set[Coord]) -> int:
    a = 0

    for coord in droplets:
        for adj in adjacent(coord):
            if adj not in droplets:
                a += 1

    return a


if __name__ == '__main__':
    print(area(load_data()[0]))
