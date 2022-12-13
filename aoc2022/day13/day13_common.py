import json

from utils import get_input_lines


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, list):
        for l_i, r_i in zip(left, right):
            cmp = compare(l_i, r_i)
            if cmp == 0:
                continue
            else:
                return cmp

        return len(left) - len(right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        raise ValueError(f"Wrong types")


def load_pairs():
    left = None
    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue

        line = json.loads(line)

        if left is None:
            left = line
        else:
            yield left, line
            left = None
