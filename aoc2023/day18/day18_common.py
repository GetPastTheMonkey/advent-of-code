from aoc2023.day10.day10_part2 import get_polygon_area
from utils import get_input_lines

NUM_TO_DIR = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}

DIRECTIONS = {
    "D": (1, 0),
    "U": (-1, 0),
    "R": (0, 1),
    "L": (0, -1),
}


def get_coords(*, part_1: bool) -> list[tuple[int, int]]:
    coords = []
    curr_pos = (0, 0)

    for line in get_input_lines(__file__):
        direction, value, color = line.split()

        if not part_1:
            value = color[2:-2]
            direction = NUM_TO_DIR[color[-2]]

        direction = DIRECTIONS[direction]
        value = int(value, 10 if part_1 else 16)

        curr_pos = (curr_pos[0] + value * direction[0], curr_pos[1] + value * direction[1])
        coords.append(curr_pos)

    return coords


def num_boundary_points(coords: list[tuple[int, int]]) -> int:
    result = 0

    for i in range(len(coords)):
        curr_coords = coords[i]
        next_coords = coords[(i + 1) % len(coords)]
        result += abs(curr_coords[0] - next_coords[0]) + abs(curr_coords[1] - next_coords[1])

    return result


def day18_solve(*, part_1: bool):
    coords = get_coords(part_1=part_1)

    # Use Pick's theorem and shoelace formula, similarly to day 10 part 2
    boundary = num_boundary_points(coords)
    area = get_polygon_area(coords)
    interior = area - (boundary // 2) + 1

    print(boundary + interior)
