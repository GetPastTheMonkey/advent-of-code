from utils import get_input_lines


def char_to_move(c: str) -> tuple[int, int]:
    return {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }[c]


def line_to_wide(line: str) -> str:
    new_line = ""

    mapping = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }

    for c in line:
        new_line += mapping[c]

    return new_line


def day15_input(*, part_1: bool) -> tuple[list[list[str]], list[tuple[int, int]], tuple[int, int]]:
    grid = []  # type: list[list[str]]
    moves = []  # type: list[tuple[int, int]]
    first_part = True
    position = (0, 0)

    for x, line in enumerate(get_input_lines(__file__)):
        if not line:
            first_part = False
        elif first_part:
            if not part_1:
                line = line_to_wide(line)

            row = []

            for y, c in enumerate(line):
                if c == "@":
                    c = "."
                    position = (x, y)

                row.append(c)

            grid.append(row)
        else:
            moves.extend(map(char_to_move, line))

    return grid, moves, position


def move(grid: list[list[str]], coords: set[tuple[int, int]], dx: int, dy: int) -> bool:
    to_check = set()  # type: set[tuple[int, int]]

    for x, y in coords:
        next_x = x + dx
        next_y = y + dy
        next_c = grid[next_x][next_y]

        if next_c == ".":
            continue
        elif next_c == "#":
            return False

        to_check.add((next_x, next_y))

        if dy == 0:
            if next_c == "[":
                to_check.add((next_x, next_y + 1))
            elif next_c == "]":
                to_check.add((next_x, next_y - 1))

    if len(to_check) > 0:
        moved = move(grid, to_check, dx, dy)

        if not moved:
            return False

    for x, y in coords:
        next_x = x + dx
        next_y = y + dy

        assert grid[next_x][next_y] == "."

        grid[next_x][next_y] = grid[x][y]
        grid[x][y] = "."

    return True


def day15_solve(*, part_1: bool) -> int:
    grid, moves, (x, y) = day15_input(part_1=part_1)

    for dx, dy in moves:
        moved = move(grid, {(x, y)}, dx, dy)

        if moved:
            x += dx
            y += dy

    s = 0

    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "O" or char == "[":
                s += 100 * x + y

    return s
