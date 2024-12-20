from collections.abc import Callable

from utils import get_input_lines


def day14_input() -> tuple[list[tuple[int, int, int, int]], int, int]:
    robots = []  # type: list[tuple[int, int, int, int]]
    max_x = -1
    max_y = -1

    for line in get_input_lines(__file__):
        p, v = line.split(" ")
        px, py = tuple(map(int, p.split("=")[1].split(",")))
        vx, vy = tuple(map(int, v.split("=")[1].split(",")))
        robots.append((px, py, vx, vy))

        max_x = max(max_x, px)
        max_y = max(max_y, py)

    return robots, max_x + 1, max_y + 1


def simulate(func: Callable[[list[tuple[int, int, int, int]], int, int, int], bool]):
    robots, width, height = day14_input()
    r = 0

    while True:
        if func(robots, width, height, r):
            break

        r += 1
        new_robots = []  # type: list[tuple[int, int, int, int]]

        for px, py, vx, vy in robots:
            new_robots.append(((px + vx) % width, (py + vy) % height, vx, vy))

        robots = new_robots
