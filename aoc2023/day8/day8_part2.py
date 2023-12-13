from aoc2023.day8.day8_common import day8_walk_until


def day8_part2() -> int:
    return day8_walk_until(
        lambda x: x.endswith("A"),
        lambda x: x.endswith("Z"),
    )


if __name__ == '__main__':
    print(day8_part2())
