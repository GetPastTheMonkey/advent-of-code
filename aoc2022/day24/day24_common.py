from queue import Queue
from typing import Tuple

from utils import get_input_lines

MOVES = [
    (0, 0),
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

LEFT = set()
RIGHT = set()
UP = set()
DOWN = set()
ROWS = 0
COLS = 0


def load_data():
    global ROWS, COLS
    nonempty_lines = filter(lambda x: len(x) > 0, get_input_lines(__file__))
    lines = list(nonempty_lines)[1:-1]
    ROWS = len(lines)
    COLS = len(lines[0][1:-1])

    for idx_line, line in enumerate(lines):
        for idx_char, char in enumerate(line[1:-1]):
            if char == ".":
                continue
            elif char == "<":
                LEFT.add((idx_line, idx_char))
            elif char == ">":
                RIGHT.add((idx_line, idx_char))
            elif char == "v":
                DOWN.add((idx_line, idx_char))
            elif char == "^":
                UP.add((idx_line, idx_char))
            else:
                raise ValueError(f"Unknown direction token: {char}")


def coord_free(coord: Tuple[int, int], time: int) -> bool:
    row, col = coord

    return not any([
        (row, (col - time) % COLS) in RIGHT,
        (row, (col + time) % COLS) in LEFT,
        ((row + time) % ROWS, col) in UP,
        ((row - time) % ROWS, col) in DOWN,
    ])


def run(start: Tuple[int, int], target: Tuple[int, int], start_time: int) -> int:
    visited = set()
    queue = Queue()

    while True:
        # Find suitable entry point
        while queue.empty():
            start_time += 1
            if coord_free(start, start_time):
                queue.put((start, start_time))

        coord, time = queue.get()

        if (coord, time) in visited:
            continue

        visited.add((coord, time))

        if coord == target:
            return time + 1

        for delta_row, delta_col in MOVES:
            new_row = coord[0] + delta_row
            new_col = coord[1] + delta_col

            if not (0 <= new_row < ROWS):
                # Would move off-grid vertically
                continue

            if not (0 <= new_col < COLS):
                # Would move off-grid horizontally
                continue

            new_coord = new_row, new_col

            if not coord_free(new_coord, time + 1):
                # Place is occupied by a blizzard next turn, cannot move there
                continue

            queue.put((new_coord, time + 1))


def day24_solve(part_1: bool) -> int:
    load_data()

    start = (0, 0)
    target = (ROWS - 1, COLS - 1)

    time = run(start, target, 0)

    if not part_1:
        time = run(target, start, time)
        time = run(start, target, time)

    return time
