from utils import get_input_lines


def cramers_rule(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> tuple[float, float]:
    det_ab = a[0] * b[1] - b[0] * a[1]
    det_ac = a[0] * c[1] - c[0] * a[1]
    det_cb = c[0] * b[1] - b[0] * c[1]

    return det_cb / det_ab, det_ac / det_ab


def line_to_tuple(line: str, c: str) -> tuple[int, int]:
    l, r = line.split(", ")

    return (
        int(l.split(c)[-1]),
        int(r.split(c)[-1]),
    )


def day13_solve(*, part_1: bool):
    s = 0

    a = (0, 0)
    b = (0, 0)

    for line in get_input_lines(__file__):
        if line.startswith("Button A"):
            a = line_to_tuple(line, "+")
        elif line.startswith("Button B"):
            b = line_to_tuple(line, "+")
        elif line.startswith("Prize"):
            c = line_to_tuple(line, "=")

            if not part_1:
                c = c[0] + 10000000000000, c[1] + 10000000000000

            x, y = cramers_rule(a, b, c)

            if x.is_integer() and y.is_integer():
                s += int(x) * 3 + int(y) * 1

    return s
