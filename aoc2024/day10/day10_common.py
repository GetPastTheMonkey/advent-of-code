from utils import get_input_lines


def day10_input() -> list[list[int]]:
    grid = []

    for line in get_input_lines(__file__):
        grid.append(list(map(int, line)))

    return grid


def walk(pos_x: int, pos_y: int, grid: list[list[int]], reached_tops: set[tuple[int, int]], task_1: bool) -> int:
    if not (0 <= pos_x < len(grid) and 0 <= pos_y < len(grid[0])):
        return 0

    value = grid[pos_x][pos_y]

    if value == 9:
        if not task_1:
            return 1
        elif (pos_x, pos_y) in reached_tops:
            return 0
        else:
            reached_tops.add((pos_x, pos_y))
            return 1

    s = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= pos_x + dx < len(grid) and 0 <= pos_y + dy < len(grid[0]) and grid[pos_x + dx][pos_y + dy] == value + 1:
            s += walk(pos_x + dx, pos_y + dy, grid, reached_tops, task_1)

    return s


def day10_solve(*, part_1: bool) -> int:
    grid = day10_input()
    s = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                s += walk(x, y, grid, set(), part_1)

    return s
