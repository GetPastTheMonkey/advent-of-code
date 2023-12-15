from aoc2023.day15.day15_common import day15_hash
from utils import get_input_lines


def main():
    s = 0

    for line in get_input_lines(__file__):
        for word in line.split(","):
            s += day15_hash(word)

    print(s)


if __name__ == '__main__':
    main()
