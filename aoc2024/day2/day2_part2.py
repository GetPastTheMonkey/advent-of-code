from itertools import combinations

from aoc2024.day2.day2_common import day2_input, is_safe


def main():
    grid = day2_input()
    s = 0

    for report in grid:
        if is_safe(report):
            s += 1
        elif any(map(lambda p: is_safe(p), combinations(report, len(report) - 1))):
            s += 1

    print(s)



if __name__ == '__main__':
    main()
