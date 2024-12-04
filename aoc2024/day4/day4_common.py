from utils import get_input_lines


def day4_input() -> list[list[str]]:
    grid = []

    for line in get_input_lines(__file__):
        grid.append(list(line))

    return grid
