"""
Implementation of creative idea by "thebadgod" on the D-INFK discord.
Compress the grid using zlib and check which round has the lowest entropy.
This is the round that probably has the Christmas tree.
"""

import zlib

from aoc2024.day14.day14_common import simulate

MIN_COMPRESS_SIZE = None


def check(robots: list[tuple[int, int, int, int]], width: int, height: int, r: int) -> bool:
    global MIN_COMPRESS_SIZE

    coords = set()

    for robot in robots:
        coords.add((robot[0], robot[1]))

    grid = ""

    for y in range(height):
        for x in range(width):
            if (x, y) in coords:
                grid += "X"
            else:
                grid += "."

        grid += "\n"

    compressed_size = len(zlib.compress(grid.encode()))

    if MIN_COMPRESS_SIZE is None or compressed_size < MIN_COMPRESS_SIZE:
        MIN_COMPRESS_SIZE = compressed_size
        print(f"--- New min compressed size of {compressed_size} in round {r} ---")

        for y in range(height):
            for x in range(width):
                if (x, y) in coords:
                    print("X", end="")
                else:
                    print(".", end="")

            print("")

    return False


if __name__ == '__main__':
    simulate(check)
