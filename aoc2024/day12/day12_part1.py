from aoc2024.day12.day12_common import get_areas


def main():
    s = 0

    for area, perimeter in get_areas():
        s += len(area) * perimeter

    print(s)


if __name__ == '__main__':
    main()
