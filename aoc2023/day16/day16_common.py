from queue import Queue

from utils import get_input_lines

Vector = tuple[int, int]


def parse_grid() -> list[list[str]]:
    grid = []  # type: list[list[str]]

    for line in get_input_lines(__file__):
        grid.append([c for c in line])

    return grid


def walk(grid: list[list[str]], position: Vector, direction: Vector) -> list[tuple[Vector, Vector]]:
    """
    Walk a single step on the grid from the current position in the current direction. After walking, turn on the
    resulting position and look in the direction of the next move. Returns the new position and the new direction.

    NOTE: Due to splitting, multiple new directions can be possible. All possibilities are returned in a list.
    """
    new_position = (position[0] + direction[0], position[1] + direction[1])

    if not (0 <= new_position[0] < len(grid)) or not (0 <= new_position[1] < len(grid[0])):
        return []

    new_char = grid[new_position[0]][new_position[1]]

    if new_char == "-" and direction[1] == 0:
        return [(new_position, (0, -1)), (new_position, (0, 1))]
    elif new_char == "|" and direction[0] == 0:
        return [(new_position, (-1, 0)), (new_position, (1, 0))]
    elif new_char == "/":
        return [(new_position, (-direction[1], -direction[0]))]
    elif new_char == "\\":
        return [(new_position, (direction[1], direction[0]))]
    else:
        return [(new_position, direction)]


def day16_energized(grid: list[list[str]], position: Vector, direction: Vector) -> int:
    seen = set()  # type: set[tuple[Vector, Vector]]
    queue = Queue()  # type: Queue[tuple[Vector, Vector]]
    queue.put(((position[0] - direction[0], position[1] - direction[1]), direction))

    while not queue.empty():
        position, direction = queue.get()

        if (position, direction) in seen:
            continue

        seen.add((position, direction))

        for w in walk(grid, position, direction):
            queue.put(w)

    # Need to subtract the initial coords (they are outside the grid)
    coords = set(x[0] for x in seen)
    return len(coords) - 1
