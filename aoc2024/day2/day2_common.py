from utils import get_input_lines


def lt(a: int, b: int) -> bool:
    return a < b


def gt(a: int, b: int) -> bool:
    return a > b


def day2_input() -> tuple[tuple[int, ...], ...]:
    grid = []  # type: list[tuple[int, ...]]

    for line in get_input_lines(__file__):
        grid.append(tuple(map(int, line.split(" "))))

    return tuple(grid)


def is_safe(report: tuple[int, ...]) -> bool:
    op = lt if report[0] < report[1] else gt
    safe = True

    for idx in range(len(report) - 1):
        if not (op(report[idx], report[idx + 1]) and 1 <= abs(report[idx] - report[idx + 1]) <= 3):
            safe = False
            break

    return safe
