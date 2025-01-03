from queue import Queue

from utils import get_input_lines


def day12_input() -> list[list[str]]:
    grid = []

    for line in get_input_lines(__file__):
        grid.append([c for c in line])

    return grid


def get_areas() -> list[tuple[set[tuple[int, int]], int]]:
    areas = []  # type: list[tuple[set[tuple[int, int]], int]]
    grid = day12_input()
    visited = set()  # type: set[tuple[int, int]]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) in visited:
                continue

            area = set()  # type: set[tuple[int, int]]
            perimeter = 0

            queue = Queue()  # type: Queue[tuple[int, int]]
            queue.put((x, y))

            while not queue.empty():
                curr_x, curr_y = queue.get()

                if (curr_x, curr_y) in area:
                    continue

                area.add((curr_x, curr_y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_x = curr_x + dx
                    next_y = curr_y + dy

                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == grid[x][y]:
                        queue.put((next_x, next_y))
                    else:
                        perimeter += 1

            areas.append((area, perimeter))
            visited |= area

    return areas
