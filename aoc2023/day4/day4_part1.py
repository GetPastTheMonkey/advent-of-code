from utils import get_input_lines


def main():
    s = 0

    for line in get_input_lines(__file__):
        winners, my_nums = line.split(": ")[1].split(" | ")

        winners = set([int(num) for num in winners.split(" ") if num])
        my_nums = set([int(num) for num in my_nums.split(" ") if num])
        correct = len(winners.intersection(my_nums))

        if correct:
            s += 2 ** (correct - 1)

    print(s)


if __name__ == '__main__':
    main()
