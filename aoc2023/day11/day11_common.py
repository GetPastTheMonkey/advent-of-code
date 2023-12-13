from utils import get_input_lines


def grid_to_coords(grid: list[list[bool]]) -> list[tuple[int, int]]:
    coords = []  # type: list[tuple[int, int]]

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell:
                coords.append((x, y))

    return coords


def parse_grid() -> tuple[list[tuple[int, int]], list[int], list[int]]:
    grid = []  # type: list[list[bool]]
    empty_rows = []  # type: list[int]
    empty_cols = []  # type: list[int]

    for row_idx, line in enumerate(get_input_lines(__file__)):
        row = [True if c == "#" else False for c in line]
        grid.append(row)

        if not any(row):
            empty_rows.append(row_idx)

    for col_idx in range(len(grid[0])):
        if not any(grid[row][col_idx] for row in range(len(grid))):
            empty_cols.append(col_idx)

    return grid_to_coords(grid), empty_rows, empty_cols


def day11_solve(*, expansion: int) -> int:
    s = 0
    coords, empty_rows, empty_cols = parse_grid()

    for i in range(len(coords)):
        x1, y1 = coords[i]

        for j in range(i + 1, len(coords)):
            x2, y2 = coords[j]

            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            num_empty_rows = len([row for row in empty_rows if min_x < row < max_x])
            num_empty_cols = len([col for col in empty_cols if min_y < col < max_y])

            s += abs(x1 - x2) + abs(y1 - y2) + (num_empty_rows + num_empty_cols) * (expansion - 1)

    return s
