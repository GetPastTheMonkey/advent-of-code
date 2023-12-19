from aoc2023.day16.day16_common import parse_grid, day16_energized


def main():
    grid = parse_grid()

    height = len(grid)
    width = len(grid[0])

    max_top = max(day16_energized(grid, (0, j), (0, 1)) for j in range(width))
    max_bottom = max(day16_energized(grid, (height - 1, j), (0, -1)) for j in range(width))
    max_left = max(day16_energized(grid, (i, 0), (0, 1)) for i in range(height))
    max_right = max(day16_energized(grid, (i, width - 1), (0, -1)) for i in range(height))

    print(max(max_top, max_bottom, max_left, max_right))


if __name__ == '__main__':
    main()
