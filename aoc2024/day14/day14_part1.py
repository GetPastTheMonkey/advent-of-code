from aoc2024.day14.day14_common import simulate


def robot_to_quadrant(robot: tuple[int, int, int, int], width: int, height: int) -> int:
    px, py, _, _ = robot

    border_x = width // 2
    border_y = height // 2

    if px == border_x or py == border_y:
        return 4

    quad = 0

    if border_x < px:
        quad += 1

    if border_y < py:
        quad += 2

    return quad


def check(robots: list[tuple[int, int, int, int]], width: int, height: int, r: int) -> bool:
    if r < 100:
        return False

    quadrants = list(map(lambda robot: robot_to_quadrant(robot, width, height), robots))
    s = 1

    for q in range(4):
        qu = len(list(filter(lambda x: x == q, quadrants)))
        s *= qu

    print(s)

    return True


if __name__ == '__main__':
    simulate(check)
