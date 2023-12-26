from queue import Queue

from utils import get_input_lines

Vector = tuple[int, int]

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]  # type: list[Vector]


def day21_parse_input() -> tuple[int, set[Vector], Vector]:
    unwalkable = set()  # type: set[Vector]
    start = (-1, -1)  # type: Vector
    size = -1

    for row, line in enumerate(get_input_lines(__file__)):
        size = len(line)
        for col, char in enumerate(line):
            if char == "S":
                start = (row, col)
            elif char == "#":
                unwalkable.add((row, col))

    assert size > 0
    return size, unwalkable, start


def day21_reachable(size: int, unwalkable: set[Vector], start: Vector):
    # Walking queue
    queue = Queue()  # type: Queue[tuple[Vector, int]]
    queue.put((start, 0))

    # Visited positions --> Don't count double
    visited = set()  # type: set[Vector]
    visited.add(start)

    # Separate counters for evens and odds (alternating)
    curr_dist = 0
    num_even_dist = 1
    num_odd_dist = 0

    while not queue.empty():
        pos, dist = queue.get()

        if dist != curr_dist:
            curr_dist = dist
            report_num = num_even_dist if dist % 2 == 0 else num_odd_dist
            yield curr_dist, report_num

        for direction in DIRECTIONS:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            new_dist = dist + 1

            new_pos_mod = (new_pos[0] % size, new_pos[1] % size)

            if new_pos_mod in unwalkable or new_pos in visited:
                # Either new position is not walkable or new position has already been visited
                continue

            visited.add(new_pos)
            queue.put((new_pos, new_dist))

            if new_dist % 2 == 0:
                num_even_dist += 1
            else:
                num_odd_dist += 1
