from collections import defaultdict
from itertools import combinations
from typing import Callable, TypeAlias

from utils import get_input_lines

coord: TypeAlias = tuple[int, int]


def day8_input() -> tuple[dict[str, list[coord]], int, int]:
    antennas = defaultdict(list)
    max_x = max_y = 0

    for x, line in enumerate(get_input_lines(__file__)):
        max_x = max(max_x, x)

        for y, char in enumerate(line):
            max_y = max(max_y, y)

            if char == '.':
                continue

            antennas[char].append((x, y))

    return antennas, max_x + 1, max_y + 1


def day8_solve(func: Callable[[coord, coord, int, int, set[coord]], None]) -> int:
    antennas_dict, height, width = day8_input()
    antinodes = set()  # type: set[coord]

    for antennas in antennas_dict.values():
        for a1, a2 in combinations(antennas, 2):
            func(a1, a2, height, width, antinodes)

    return len(antinodes)
