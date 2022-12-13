from aoc2022.day13.day13_common import load_pairs, compare


def main():
    counter = 0

    for idx, (left, right) in enumerate(load_pairs()):
        if compare(left, right) < 0:
            # Add 1 additionally because puzzle starts with index 1
            counter += idx + 1

    print(counter)


if __name__ == '__main__':
    main()
