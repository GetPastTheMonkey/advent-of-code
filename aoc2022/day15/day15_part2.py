from aoc2022.day15.day15_common import load_data


def main():
    sensors, _ = load_data()
    limit = 4000000

    for y in range(limit + 1):
        x = 0
        changed = True

        while changed:
            changed = False

            for s_x, s_y, radius in sensors:
                dist = abs(s_x - x) + abs(s_y - y)

                if dist <= radius:
                    x = s_x + radius - abs(s_y - y) + 1
                    changed = True

        if x <= limit:
            print(4000000 * x + y)
            break


if __name__ == '__main__':
    main()
