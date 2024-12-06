from utils import get_input_lines

DIRECTIONS = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1)  # Left
]


def day6_input() -> tuple[set[tuple[int, int]], tuple[int, int], int, int, int]:
    obstacles = set()  # type: set[tuple[int, int]]
    start = (0, 0)  # type: tuple[int, int]
    max_x = 0
    max_y = 0

    for x, line in enumerate(get_input_lines(__file__)):
        for y, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                start = (x, y)

        max_x = x
        max_y = len(line)

    return obstacles, start, 0, max_x + 1, max_y + 1


def run_guard(obstacles, start_pos, start_dir, height, width) -> tuple[int, bool]:
    visited = set()
    states = set()

    curr_pos = start_pos
    curr_dir = start_dir
    found_loop = False

    while True:
        visited.add(curr_pos)
        curr_state = (curr_pos[0], curr_pos[1], curr_dir)

        if curr_state in states:
            found_loop = True
            break

        states.add(curr_state)

        new_pos = (
            curr_pos[0] + DIRECTIONS[curr_dir][0],
            curr_pos[1] + DIRECTIONS[curr_dir][1]
        )

        if not (0 <= new_pos[0] < height and 0 <= new_pos[1] < width):
            break
        elif new_pos in obstacles:
            curr_dir = (curr_dir + 1) % len(DIRECTIONS)
        else:
            curr_pos = new_pos

    return len(visited), found_loop
