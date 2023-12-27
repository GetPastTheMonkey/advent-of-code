from utils import get_input_lines

Vector = tuple[int, int]


def day23_parse_grid() -> list[list[str]]:
    grid = []  # type: list[list[str]]

    for line in get_input_lines(__file__):
        grid.append([c for c in line])

    return grid
