from functools import cache

from utils import get_input_lines

_PATTERNS = []  # type: list[str]


def day19_input() -> list[str]:
    global _PATTERNS
    towels = []  # type: list[str]
    first_part = True

    for line in get_input_lines(__file__):
        if not line:
            first_part = False
        elif first_part:
            _PATTERNS = line.split(", ")
        else:
            towels.append(line)

    return towels


@cache
def count_ways(wanted: str) -> int:
    count = 0

    for pattern in _PATTERNS:
        if wanted == pattern:
            count += 1
        elif wanted.startswith(pattern):
            count += count_ways(wanted[len(pattern):])

    return count


def day19_solve(*, part_1: bool) -> int:
    towels = day19_input()
    s = 0

    for towel in towels:
        ways = count_ways(towel)

        if part_1 and ways > 0:
            ways = 1

        s += ways

    return s
