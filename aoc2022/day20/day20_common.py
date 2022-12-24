from typing import List, Tuple

from utils import get_input_lines


def load_data(multiplier: int) -> List[Tuple[int, int]]:
    non_empty_lines = filter(lambda l: len(l) > 0, get_input_lines(__file__))
    lines_to_ints = map(int, non_empty_lines)
    multiplied = map(lambda x: multiplier * x, lines_to_ints)
    enumerated = enumerate(multiplied)
    return list(enumerated)


def day20_solve(part_1: bool) -> int:
    data = load_data(1 if part_1 else 811589153)
    len_data = len(data)

    for mix_count in range(1 if part_1 else 10):
        for i in range(len_data):
            for j in range(len_data):
                if data[j][0] == i:
                    number = data[j]
                    data.pop(j)

                    if number[1] == -j:
                        data.append(number)
                    else:
                        data.insert((j + number[1]) % (len_data - 1), number)
                    break

    # Find index with value 0
    for i in range(len_data):
        if data[i][1] == 0:
            # Sum of 1000th, 2000th, and 3000th elements in circular list after value 0
            return sum([data[(i + a) % len_data][1] for a in [1000, 2000, 3000]])

    raise ValueError(f"Value 0 is not in the list")
