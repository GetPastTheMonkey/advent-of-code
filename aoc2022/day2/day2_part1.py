from utils import get_input_lines


def main():
    points = 0

    for line in get_input_lines(__file__):
        elf, me = line.split(" ")
        elf, me = ord(elf) - ord("A") + 1, ord(me) - ord("X") + 1

        points += me

        if elf == me:
            points += 3
        elif elf % 3 == (me - 1) % 3:
            points += 6

    print(points)


if __name__ == '__main__':
    main()
