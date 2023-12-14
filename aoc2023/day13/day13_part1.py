from aoc2023.day13.day13_common import get_grids, find_mirrors, scoring


def main():
    s = 0

    for grid in get_grids():
        horizontal, vertical = find_mirrors(grid)
        s += scoring(horizontal, vertical)

    print(s)


if __name__ == '__main__':
    main()
