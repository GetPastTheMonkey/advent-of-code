from hashlib import md5
from queue import Queue
from typing import Union

PASSWORD = "veumntbg"
ROWS, COLS = 4, 4
DIRECTIONS = [
    ("U", -1, 0),
    ("D", 1, 0),
    ("L", 0, -1),
    ("R", 0, 1),
]


def day17_solve(part_1: bool) -> Union[str, int]:
    queue = Queue()
    queue.put((0, 0, ""))
    longest_path_len = 0

    while not queue.empty():
        pos_x, pos_y, path = queue.get()

        if pos_x == ROWS - 1 and pos_y == COLS - 1:
            if part_1:
                return path

            longest_path_len = max(len(path), longest_path_len)
            continue

        for idx, char in enumerate(md5((PASSWORD + path).encode()).hexdigest()[:4]):
            if char.isdigit() or char == "a":
                # The door in this direction is closed
                continue

            next_step, dx, dy = DIRECTIONS[idx]
            next_x = pos_x + dx
            next_y = pos_y + dy

            if not (0 <= next_x < ROWS):
                # The move would be outside the grid in the X axis
                continue

            if not (0 <= next_y < COLS):
                # The move would be outside the grid in the Y axis
                continue

            queue.put((next_x, next_y, path + next_step))

    return longest_path_len
