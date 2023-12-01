from utils import get_input_lines


def main():
    s = 0

    for line in get_input_lines(__file__):
        nums = [c for c in line if c.isdigit()]
        s += int("".join([nums[0], nums[-1]]))

    print(s)


if __name__ == '__main__':
    main()
