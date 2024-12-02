from aoc2024.day1.day1_common import day1_input


def main():
    list_1, list_2 = day1_input()
    s = 0

    for val_1 in list_1:
        s += val_1 * list_2.count(val_1)

    print(s)


if __name__ == '__main__':
    main()
