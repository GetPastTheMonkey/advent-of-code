from functools import cmp_to_key

from aoc2022.day13.day13_common import load_pairs, compare


def main():
    el_2 = [[2]]
    el_6 = [[6]]
    packets = [el_2, el_6]

    for pair in load_pairs():
        packets.extend(pair)

    packets = sorted(packets, key=cmp_to_key(compare))

    # Add 1 because puzzle is 1-indexed
    idx_2 = packets.index(el_2) + 1
    idx_6 = packets.index(el_6) + 1

    print(idx_2 * idx_6)


if __name__ == '__main__':
    main()
