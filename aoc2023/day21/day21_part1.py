from aoc2023.day21.day21_common import day21_parse_input, day21_reachable


def main():
    max_dist = 64
    size, unwalkable, start = day21_parse_input()

    for dist, num_reachable in day21_reachable(size, unwalkable, start):
        if dist == max_dist:
            print(num_reachable)
            break


if __name__ == '__main__':
    main()
