import operator
from functools import reduce

from utils import get_input_lines


def main():
    s = 0

    for line in get_input_lines(__file__):
        maximums = dict()

        for draw in line.split(": ")[1].split("; "):
            for amount, color in map(lambda x: x.split(" "), draw.split(", ")):
                if color not in maximums or maximums[color] < int(amount):
                    maximums[color] = int(amount)

        s += reduce(operator.mul, maximums.values(), 1)

    print(s)


if __name__ == '__main__':
    main()
