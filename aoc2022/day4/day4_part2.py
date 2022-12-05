from utils import get_input_lines


def main():
    containments = 0

    for line in get_input_lines(__file__):
        range_a, range_b = line.split(",")
        range_a_l, range_a_r = map(int, range_a.split("-"))
        range_b_l, range_b_r = map(int, range_b.split("-"))

        if range_a_l <= range_b_l <= range_a_r or range_a_l <= range_b_r <= range_a_r:
            containments += 1
        elif range_b_l <= range_a_l <= range_b_r or range_b_l <= range_a_r <= range_b_r:
            containments += 1

    print(containments)


if __name__ == '__main__':
    main()
