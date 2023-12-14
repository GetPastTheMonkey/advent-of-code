from aoc2023.day14.day14_common import parse_grid, tilt_north, grid_weight


def main():
    grid = parse_grid()
    tilt_north(grid)
    w = grid_weight(grid)
    print(w)


if __name__ == '__main__':
    main()
