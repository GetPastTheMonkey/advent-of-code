from enum import Enum

from utils import get_input_lines


class Tile(Enum):
    GROUND = "."
    PIPE_NS = "|"
    PIPE_EW = "-"
    PIPE_NE = "L"
    PIPE_NW = "J"
    PIPE_SW = "7"
    PIPE_SE = "F"


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


def parse_grid() -> tuple[list[list[Tile]], tuple[int, int]]:
    grid = []
    start = None

    for row, line in enumerate(get_input_lines(__file__)):
        curr_row = []

        for col, char in enumerate(line):
            if char == "|":
                curr_row.append(Tile.PIPE_NS)
            elif char == "-":
                curr_row.append(Tile.PIPE_EW)
            elif char == "L":
                curr_row.append(Tile.PIPE_NE)
            elif char == "J":
                curr_row.append(Tile.PIPE_NW)
            elif char == "7":
                curr_row.append(Tile.PIPE_SW)
            elif char == "F":
                curr_row.append(Tile.PIPE_SE)
            elif char == ".":
                curr_row.append(Tile.GROUND)
            elif char == "S":
                curr_row.append(Tile.GROUND)
                start = (row, col)
            else:
                raise ValueError(f"Unknown character at position ({row}, {col}): {char}")

        grid.append(curr_row)

    if start is None:
        raise ValueError("No starting tile found")

    # Determine pipe at starting position
    top_connected = grid[start[0] - 1][start[1]] in [Tile.PIPE_NS, Tile.PIPE_SE, Tile.PIPE_SW]
    bottom_connected = grid[start[0] + 1][start[1]] in [Tile.PIPE_NS, Tile.PIPE_NE, Tile.PIPE_NW]
    left_connected = grid[start[0]][start[1] - 1] in [Tile.PIPE_EW, Tile.PIPE_NE, Tile.PIPE_SE]
    right_connected = grid[start[0]][start[1] + 1] in [Tile.PIPE_EW, Tile.PIPE_NW, Tile.PIPE_SW]

    if top_connected and bottom_connected:
        center_pipe = Tile.PIPE_NS
    elif top_connected and left_connected:
        center_pipe = Tile.PIPE_NW
    elif top_connected and right_connected:
        center_pipe = Tile.PIPE_NE
    elif bottom_connected and left_connected:
        center_pipe = Tile.PIPE_SW
    elif bottom_connected and right_connected:
        center_pipe = Tile.PIPE_SE
    elif left_connected and right_connected:
        center_pipe = Tile.PIPE_EW
    else:
        raise ValueError("Unknown pipe at starting position")

    grid[start[0]][start[1]] = center_pipe
    return grid, start


def walk(grid: list[list[Tile]], position: tuple[int, int], direction: Direction) -> tuple[tuple[int, int], Direction]:
    if direction == Direction.UP:
        new_position = (position[0] - 1, position[1])
    elif direction == Direction.DOWN:
        new_position = (position[0] + 1, position[1])
    elif direction == Direction.LEFT:
        new_position = (position[0], position[1] - 1)
    elif direction == Direction.RIGHT:
        new_position = (position[0], position[1] + 1)
    else:
        raise ValueError("Invalid direction")

    # Get new direction from current direction and tile at new position
    tile = grid[new_position[0]][new_position[1]]
    new_direction = None

    if direction == Direction.UP:
        if tile == Tile.PIPE_NS:
            new_direction = Direction.UP
        elif tile == Tile.PIPE_SE:
            new_direction = Direction.RIGHT
        elif tile == Tile.PIPE_SW:
            new_direction = Direction.LEFT
    elif direction == Direction.LEFT:
        if tile == Tile.PIPE_EW:
            new_direction = Direction.LEFT
        elif tile == Tile.PIPE_NE:
            new_direction = Direction.UP
        elif tile == Tile.PIPE_SE:
            new_direction = Direction.DOWN
    elif direction == Direction.DOWN:
        if tile == Tile.PIPE_NS:
            new_direction = Direction.DOWN
        elif tile == Tile.PIPE_NW:
            new_direction = Direction.LEFT
        elif tile == Tile.PIPE_NE:
            new_direction = Direction.RIGHT
    elif direction == Direction.RIGHT:
        if tile == Tile.PIPE_EW:
            new_direction = Direction.RIGHT
        elif tile == Tile.PIPE_NW:
            new_direction = Direction.UP
        elif tile == Tile.PIPE_SW:
            new_direction = Direction.DOWN

    if new_direction is None:
        raise ValueError("Could not find new direction")

    return new_position, new_direction


def day10_loop_coords() -> list[tuple[int, int]]:
    grid, start = parse_grid()

    # Determine initial direction
    if grid[start[0]][start[1]] in [Tile.PIPE_NE, Tile.PIPE_NS, Tile.PIPE_NW]:
        direction = Direction.UP
    elif grid[start[0]][start[1]] in [Tile.PIPE_SW, Tile.PIPE_SE]:
        direction = Direction.DOWN
    elif grid[start[0]][start[1]] in [Tile.PIPE_EW]:
        direction = Direction.RIGHT
    else:
        raise ValueError("No correct direction for starting position")

    # Walk once to make loop condition easier
    position, direction = walk(grid, start, direction)
    visited = [position]

    while position != start:
        position, direction = walk(grid, position, direction)
        visited.append(position)

    return visited
