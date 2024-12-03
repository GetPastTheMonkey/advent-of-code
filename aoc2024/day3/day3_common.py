import re

from utils import get_input_lines


def day3_solve(*, part_1: bool) -> int:
    s = 0
    enabled = True

    for line in get_input_lines(__file__):
        for m in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            if m[0] == "do()":
                enabled = True
            elif m[0] == "don't()":
                enabled = False
            elif enabled or part_1:
                mul1, mul2 = map(int, m[0][4:-1].split(","))
                s += mul1 * mul2

    return s
