from queue import Queue

from utils import get_input_lines

DIRECTIONS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

TURN_LEFT = {
    "N": "W",
    "E": "N",
    "S": "E",
    "W": "S",
}

TURN_RIGHT = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}


def day16_input() -> list[list[str]]:
    grid = []  # type: list[list[str]]

    for line in get_input_lines(__file__):
        grid.append(list(line))

    return grid


def day16_solve(*, part_1: bool) -> int:
    grid = day16_input()
    min_cost_dict = dict()  # type: dict[tuple[int, int, str], int]
    min_cost = float("inf")
    min_coords = set()  # type: set[tuple[int, int]]

    queue = Queue()  # type: Queue[tuple[int, int, str, int, set[tuple[int, int]]]]
    queue.put((len(grid) - 2, 1, "E", 0, {(len(grid) - 2, 1)}))

    while not queue.empty():
        pos_x, pos_y, direction, cost, visited = queue.get()

        if (pos_x, pos_y, direction) in min_cost_dict and min_cost_dict[(pos_x, pos_y, direction)] < cost:
            continue

        min_cost_dict[(pos_x, pos_y, direction)] = cost

        if grid[pos_x][pos_y] == "E":
            if cost == min_cost:
                min_coords = min_coords | visited
            elif cost < min_cost:
                min_cost = cost
                min_coords = visited
            continue

        # OPTION 1: Go straight if possible
        dx, dy = DIRECTIONS[direction]
        new_pos_x = pos_x + dx
        new_pos_y = pos_y + dy

        if grid[new_pos_x][new_pos_y] != "#":
            queue.put((new_pos_x, new_pos_y, direction, cost + 1, visited | {(new_pos_x, new_pos_y)}))

        # OPTION 2: Turn left
        queue.put((pos_x, pos_y, TURN_LEFT[direction], cost + 1000, visited))

        # OPTION 3: Turn right
        queue.put((pos_x, pos_y, TURN_RIGHT[direction], cost + 1000, visited))

    return min_cost if part_1 else len(min_coords)
