from aoc2022.day15.day15_common import load_data


def main():
    sensors, beacons = load_data()
    row = 2000000
    x_cannot_be = set()

    for s_x, s_y, radius in sensors:
        available_dist = radius - abs(s_y - row)
        if available_dist > 0:
            for i in range(available_dist + 1):
                if (s_x + i, row) not in beacons:
                    x_cannot_be.add(s_x + i)

                if (s_x - i, row) not in beacons:
                    x_cannot_be.add(s_x - i)

    print(len(x_cannot_be))


if __name__ == '__main__':
    main()
