from aoc2024.day1.day1_common import day1_input


def main():
    list_1, list_2 = day1_input()
    s = 0

    for x, y in zip(list_1, list_2):
        s += abs(x - y)

    print(s)


if __name__ == '__main__':
    main()
