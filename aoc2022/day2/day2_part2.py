from utils import get_input_lines


def main():
    points = 0

    for line in get_input_lines(__file__):
        elf, outcome = line.split(" ")
        elf, outcome = ord(elf) - ord("A") + 1, (ord(outcome) - ord("X") - 1) % 3

        points += (((elf + outcome) - 1) % 3) + 1
        points += 3 * ((outcome + 1) % 3)

    print(points)


if __name__ == '__main__':
    main()
