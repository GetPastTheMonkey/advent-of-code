from aoc2023.day16.day16_common import parse_grid, day16_energized


def main():
    grid = parse_grid()
    result = day16_energized(grid, (0, 0), (0, 1))
    print(result)


if __name__ == '__main__':
    main()
