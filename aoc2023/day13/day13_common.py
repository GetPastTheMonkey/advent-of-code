from utils import get_input_lines


def find_horizontal_mirrors(grid: list[list[bool]]) -> list[int]:
    result = []  # type: list[int]

    for mirror_idx in range(len(grid) - 1):
        i = mirror_idx
        j = mirror_idx + 1

        mirror = True

        while i >= 0 and j < len(grid):
            if not all(x == y for x, y in zip(grid[i], grid[j])):
                mirror = False
                break

            i -= 1
            j += 1

        if mirror:
            result.append(mirror_idx)

    return result


def find_mirrors(grid: list[list[bool]]) -> tuple[list[int], list[int]]:
    horizontal_mirrors = find_horizontal_mirrors(grid)
    vertical_mirrors = find_horizontal_mirrors(list(zip(*grid)))
    return horizontal_mirrors, vertical_mirrors


def get_grids():
    current_grid = []  # type: list[list[bool]]

    for line in get_input_lines(__file__):
        if len(line) == 0:
            yield current_grid
            current_grid = []
        else:
            current_grid.append([c == "." for c in line])

    if len(current_grid) > 0:
        yield current_grid


def scoring(horizontal: list[int], vertical: list[int]) -> int:
    return 100 * (sum(horizontal) + len(horizontal)) + sum(vertical) + len(vertical)
