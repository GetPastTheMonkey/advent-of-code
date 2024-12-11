from collections import defaultdict

from utils import get_input_lines


def day11_input() -> tuple[set[int], dict[int, int]]:
    line = next(get_input_lines(__file__))
    stones = set()
    mult = defaultdict(int)

    for s in map(int, line.split(" ")):
        stones.add(s)
        mult[s] += 1

    return stones, mult


def blink(stones: set[int], mult: dict[int, int]) -> tuple[set[int], dict[int, int]]:
    new_stones = set()
    new_mult = defaultdict(int)

    for stone in stones:
        if stone == 0:
            new_stones.add(1)
            new_mult[1] += mult[stone]
            continue

        stone_str = str(stone)
        stone_len = len(stone_str)

        if stone_len % 2 == 0:
            stone_l = int(stone_str[:stone_len // 2])
            stone_r = int(stone_str[stone_len // 2:])

            new_stones.add(stone_l)
            new_stones.add(stone_r)

            new_mult[stone_l] += mult[stone]
            new_mult[stone_r] += mult[stone]
        else:
            new_stone = 2024 * stone
            new_stones.add(new_stone)
            new_mult[new_stone] += mult[stone]

    return new_stones, new_mult


def day11_solve(*, part_1: bool) -> int:
    stones, mult = day11_input()

    for i in range(25 if part_1 else 75):
        stones, mult = blink(stones, mult)

    return sum(mult.values())
