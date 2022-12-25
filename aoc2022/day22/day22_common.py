from typing import List, Generator, Tuple, Any, Optional

from utils import get_input

VOID, WALL, OPEN = range(3)

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def parse_grid(grid_lines: List[str]) -> List[List[int]]:
    width = max(map(lambda x: len(x), grid_lines))
    grid = [[VOID] * width for _ in range(len(grid_lines))]

    for line_idx, line in enumerate(grid_lines):
        for char_idx, char in enumerate(line):
            if char == ".":
                grid[line_idx][char_idx] = OPEN
            elif char == "#":
                grid[line_idx][char_idx] = WALL

    return grid


def parse_movement(movement_str: str) -> Generator[Tuple[int, Optional[str]], Any, None]:
    char_buf = ""

    for char in movement_str:
        if char.isdigit():
            char_buf += char
        else:
            yield int(char_buf), char
            char_buf = ""

    yield int(char_buf), None


def load_data():
    grid_lines = []
    movement_str = ""
    parsing_grid = True

    # Parse input data
    with get_input(__file__) as f:
        for line in f:
            if parsing_grid:
                if len(line.strip()) == 0:
                    parsing_grid = False
                else:
                    grid_lines.append(line.rstrip())
            elif len(movement_str) == 0:
                movement_str = line.strip()

    grid = parse_grid(grid_lines)
    movement = parse_movement(movement_str)

    # Get starting position in top row (first open tile)
    position = (0, grid[0].index(OPEN))

    # Return everything
    return grid, position, movement
