from utils import get_input_lines


SAFE_CHAR = "."
TRAP_CHAR = "^"


def count_safe(line: str) -> int:
    return sum(1 if c == SAFE_CHAR else 0 for c in line)


def next_row(line: str) -> str:
    new_line = []

    for idx in range(len(line)):
        left_safe = line[idx - 1] == SAFE_CHAR if idx > 0 else True
        right_safe = line[idx + 1] == SAFE_CHAR if idx < len(line) - 1 else True
        center_safe = line[idx] == SAFE_CHAR

        if not left_safe and not center_safe and right_safe:
            new_safe = False
        elif not center_safe and not right_safe and left_safe:
            new_safe = False
        elif not left_safe and center_safe and right_safe:
            new_safe = False
        elif not right_safe and center_safe and left_safe:
            new_safe = False
        else:
            new_safe = True

        new_line.append(SAFE_CHAR if new_safe else TRAP_CHAR)

    return "".join(new_line)


def day18_solve(rows):
    for line in get_input_lines(__file__):
        nr_safe = count_safe(line)
        curr_line = line

        for _ in range(rows - 1):
            curr_line = next_row(curr_line)
            nr_safe += count_safe(curr_line)

        print(nr_safe)
