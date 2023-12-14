from enum import Enum

from utils import get_input_lines


class Tile(Enum):
    GROUND = "."
    ROUND = "O"
    SQUARE = "#"


Grid = list[list[Tile]]


def char_to_tile(char: str) -> Tile:
    if char == ".":
        return Tile.GROUND
    elif char == "O":
        return Tile.ROUND
    elif char == "#":
        return Tile.SQUARE
    else:
        raise ValueError(f"Unknown character: {char}")


def parse_grid() -> Grid:
    grid = []  # type: Grid

    for line in get_input_lines(__file__):
        grid.append(list(map(char_to_tile, line)))

    return grid


def tilt_north(grid: Grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == Tile.ROUND:
                new_i = i

                while new_i - 1 >= 0 and grid[new_i - 1][j] == Tile.GROUND:
                    new_i -= 1

                if new_i < i:
                    grid[new_i][j] = Tile.ROUND
                    grid[i][j] = Tile.GROUND


def grid_weight(grid: Grid) -> int:
    s = 0

    for i in range(len(grid)):
        weight = len(grid) - i
        s += sum(weight for c in grid[i] if c == Tile.ROUND)

    return s
