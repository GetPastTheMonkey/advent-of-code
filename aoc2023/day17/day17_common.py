import heapq

from utils import get_input_lines

Vector = tuple[int, int]

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]  # type: list[Vector]


def parse_grid() -> list[list[int]]:
    grid = []  # type: list[list[int]]

    for line in get_input_lines(__file__):
        grid.append([int(c) for c in line])

    return grid


def day17_solve(*, part_1: bool) -> int:
    grid = parse_grid()
    height = len(grid)
    width = len(grid[0])
    best = dict()

    min_straight = 0 if part_1 else 4
    max_straight = 3 if part_1 else 10

    # Heap item structure: (heat, position, direction, straight)
    # Initially, direction is (0, 0), so all directions are explored
    heap = [(0, (0, 0), (0, 0), 0)]

    while heap:
        heat, position, curr_direction, curr_straight = heapq.heappop(heap)  # type: int, Vector, Vector, int

        if position == (height - 1, width - 1) and curr_straight >= min_straight:
            return heat

        for direction in DIRECTIONS:
            if 0 != direction[0] == -curr_direction[0] or 0 != direction[1] == -curr_direction[1]:
                # Skip, turnaround not allowed!
                continue

            if direction != curr_direction != (0, 0) and curr_straight < min_straight:
                # Skip, straight is too short!
                # NOTE: The condition "curr_direction != (0, 0)" filters out the starting position
                continue

            if direction == curr_direction:
                new_straight = curr_straight + 1

                if new_straight > max_straight:
                    # Skip, straight too long!
                    continue
            else:
                new_straight = 1

            new_position = (position[0] + direction[0], position[1] + direction[1])

            if not (0 <= new_position[0] < height and 0 <= new_position[1] < width):
                # Skip, new position not in grid!
                continue

            # Valid position --> Add to heap
            new_heat = heat + grid[new_position[0]][new_position[1]]

            best_key = (new_position, direction, new_straight)

            if best_key in best and best[best_key] <= new_heat:
                # Skip, already found a cheaper way to get here!
                continue

            best[best_key] = new_heat

            heapq.heappush(heap, (new_heat, new_position, direction, new_straight))

    raise ValueError("There is no way to the end position!")
