from aoc2024.day14.day14_common import simulate


def check(robots: list[tuple[int, int, int, int]], width: int, height: int, r: int) -> bool:
    coords = set()

    for robot in robots:
        coords.add((robot[0], robot[1]))

    for y in range(height):
        count = 0

        for x in range(1, width):
            if (x - 1, y) in coords and (x, y) in coords:
                count += 1

        if count > 20:
            # If there is a line of more than 20 robots, this is probably the Christmas tree
            print(r)
            return True

    return False


if __name__ == '__main__':
    simulate(check)
