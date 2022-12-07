from queue import Queue
from typing import List, Tuple

FAVOURITE_NUMBER = 1364
TARGET = (31, 39)
MAX_DISTANCE = 50


def is_open(x: int, y: int) -> bool:
    val = x*x + 3*x + 2*x*y + y + y*y + FAVOURITE_NUMBER
    nonzero_bits = bin(val).count("1")
    return nonzero_bits % 2 == 0


def neighbours(x: int, y: int) -> List[Tuple[int, int]]:
    n = [
        (x + 1, y),  # Always go down
        (x, y + 1)   # Always go right
    ]

    if x > 0:
        # If not at the top, go up
        n.append((x - 1, y))

    if y > 0:
        # If not on the left side, go right
        n.append((x, y - 1))

    return n


def free_neighbours(x: int, y: int):
    return filter(lambda pos: is_open(*pos), neighbours(x, y))


def day13_solve(part_1: bool) -> int:
    queue = Queue()
    queue.put(((1, 1), 0))
    visited = dict()

    while True:
        curr_pos, dist = queue.get(block=False)
        dist += 1

        # Check if already visited this
        if curr_pos in visited:
            continue

        visited[curr_pos] = dist

        if part_1 and curr_pos == TARGET:
            return dist - 1

        if not part_1 and dist > MAX_DISTANCE:
            return len(visited)

        # Add all free neighbours to the queue (if not already visited)
        for n in free_neighbours(*curr_pos):
            if n not in visited:
                queue.put((n, dist))
