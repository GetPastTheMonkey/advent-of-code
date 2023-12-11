from aoc2023.day6.day6_common import day6_solve


def parse_line(line):
    return map(int, filter(lambda x: len(x) > 0, line.split(" ")))


def main():
    print(day6_solve(parse_line))


if __name__ == '__main__':
    main()
