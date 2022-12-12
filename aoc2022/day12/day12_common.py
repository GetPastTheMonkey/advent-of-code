from queue import Queue
from typing import Tuple, List

from utils import get_input_lines

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def load_grid(part_1: bool) -> Tuple[List[List[int]], List[Tuple[int, int]], Tuple[int, int]]:
    grid = []
    starts = []
    end = 0, 0

    for x, line in enumerate(get_input_lines(__file__)):
        chars = []

        for y, char in enumerate(line):
            if not part_1 and char == "a":
                # For part 2: Pretend that all "a" are actually starts
                char = "S"

            if char == "S":
                starts.append((x, y))
                char = "a"
            elif char == "E":
                end = x, y
                char = "z"

            chars.append(ord(char) - ord("a"))

        if len(chars) > 0:
            grid.append(chars)

    return grid, starts, end


def day12_solve(part_1: bool) -> int:
    grid, starts, end = load_grid(part_1)
    height = len(grid)
    width = len(grid[0])
    shortest = None

    while len(starts) > 0:
        visited = set()
        queue = Queue()
        queue.put((starts.pop(), 0))

        while not queue.empty():
            pos, history = queue.get(block=False)

            if pos in visited:
                continue

            visited.add(pos)

            if pos == end:
                if shortest is None or history < shortest:
                    shortest = history
                break

            for direction in DIRECTIONS:
                new_pos = pos[0] + direction[0], pos[1] + direction[1]

                if not (0 <= new_pos[0] < height) or not (0 <= new_pos[1] < width):
                    # New position is outside the grid
                    continue

                if grid[new_pos[0]][new_pos[1]] - grid[pos[0]][pos[1]] > 1:
                    # Height at new position is more than 1 higher than at current position
                    continue

                if new_pos not in visited:
                    queue.put((new_pos, history + 1))

    return shortest
