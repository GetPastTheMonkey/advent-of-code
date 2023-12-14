from aoc2023.day14.day14_common import parse_grid, Tile, Grid, tilt_north, grid_weight


def tilt_south(grid: Grid):
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0])):
            if grid[i][j] == Tile.ROUND:
                new_i = i

                while new_i + 1 < len(grid) and grid[new_i + 1][j] == Tile.GROUND:
                    new_i += 1

                if new_i > i:
                    grid[new_i][j] = Tile.ROUND
                    grid[i][j] = Tile.GROUND


def tilt_west(grid: Grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == Tile.ROUND:
                new_j = j

                while new_j - 1 >= 0 and grid[i][new_j - 1] == Tile.GROUND:
                    new_j -= 1

                if new_j < j:
                    grid[i][new_j] = Tile.ROUND
                    grid[i][j] = Tile.GROUND


def tilt_east(grid: Grid):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == Tile.ROUND:
                new_j = j

                while new_j + 1 < len(grid[0]) and grid[i][new_j + 1] == Tile.GROUND:
                    new_j += 1

                if new_j > j:
                    grid[i][new_j] = Tile.ROUND
                    grid[i][j] = Tile.GROUND


def tilt_cycle(grid: Grid):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)


def grid_repr(grid: Grid) -> str:
    return "".join("".join(c.value for c in row) for row in grid)


def main():
    grid = parse_grid()
    weight_map = dict()
    order = []

    while True:
        tilt_cycle(grid)
        grid_str = grid_repr(grid)

        if grid_str in weight_map:
            cycle_start = order.index(grid_str)
            cycle_length = len(order) - cycle_start
            final_offset = ((1000000000 - cycle_start - 1) % cycle_length) + cycle_start
            result = weight_map[order[final_offset]]
            print(result)
            break

        weight_map[grid_str] = grid_weight(grid)
        order.append(grid_str)


if __name__ == '__main__':
    main()
