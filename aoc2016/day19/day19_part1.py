import math

from aoc2016.day19.day19_common import ELVES


def main() -> int:
    # See: https://de.wikipedia.org/wiki/Josephus-Problem
    a = math.floor(math.log2(ELVES))
    b = ELVES - (2 ** a)
    return (2 * b) + 1


if __name__ == '__main__':
    print(main())
