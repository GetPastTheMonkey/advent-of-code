from aoc2024.day6.day6_common import day6_input, run_guard


def main():
    obstacles, start, direction, height, width = day6_input()
    s = 0

    for x in range(height):
        for y in range(width):
            if (x, y) in obstacles | {start}:
                continue

            new_obstacles = obstacles.copy() | {(x, y)}
            has_loop = run_guard(new_obstacles, start, direction, height, width)[1]

            if has_loop:
                s += 1

        print(f"Checked {x + 1}/{height} rows ({s = })")

    print(s)


if __name__ == '__main__':
    main()
