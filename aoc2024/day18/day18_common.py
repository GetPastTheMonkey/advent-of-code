from queue import Queue

from utils import get_input_lines


def day18_input() -> list[tuple[int, int]]:
    coords = []  # type: list[tuple[int, int]]

    for line in get_input_lines(__file__):
        x, y = map(int, line.split(","))
        coords.append((x, y))

    return coords


def day18_shortest_path(coords: set[tuple[int, int]], end: int):
    end_x, end_y = end, end

    queue = Queue()  # type: Queue[tuple[int, int, list[tuple[int, int]]]]
    queue.put((0, 0, []))

    visited = set()  # type: set[tuple[int, int]]

    while not queue.empty():
        x, y, path = queue.get()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == end_x and y == end_y:
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x <= end_x and 0 <= new_y <= end_y and (x, y) not in coords:
                queue.put((new_x, new_y, path + [(x, y)]))

    return []
