from aoc2024.day22.day22_common import get_secrets
from utils import get_input_lines


def main():
    s = 0

    for line in get_input_lines(__file__):
        s += get_secrets(int(line))[-1]

    print(s)


if __name__ == '__main__':
    main()
