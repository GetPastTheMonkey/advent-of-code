from utils import get_input_lines


def is_solvable(current: int, parts: list[int], result: int, part_1: bool) -> bool:
    if len(parts) == 0:
        return current == result
    elif current > result:
        # Values are strictly increasing --> Cannot make smaller
        return False

    head = parts[0]
    tail = parts[1:]

    return is_solvable(current + head, tail, result, part_1) or \
        is_solvable(current * head, tail, result, part_1) or \
        (not part_1 and is_solvable(int(str(current) + str(head)), tail, result, part_1))


def day7_solve(*, part_1: bool) -> int:
    s = 0

    for line in get_input_lines(__file__):
        result_str, parts_str = line.split(": ")
        result = int(result_str)
        parts = list(map(int, parts_str.split(" ")))

        if len(parts) > 0:
            head = parts[0]
            tail = parts[1:]

            if is_solvable(head, tail, result, part_1):
                s += result

    return s
