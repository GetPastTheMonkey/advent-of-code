import math

from utils import get_input_lines


def day6_solve(parse_line) -> int:
    prod = 1
    t_s = []
    d_s = []

    for line in get_input_lines(__file__):
        if line.startswith("T"):
            t_s = parse_line(line[5:])
        elif line.startswith("D"):
            d_s = parse_line(line[9:])

    for t, d in zip(t_s, d_s):
        lower = int((t - math.sqrt(t**2 - 4 * d)) // 2) + 1
        upper = t - lower
        prod *= upper - lower + 1

    return prod
