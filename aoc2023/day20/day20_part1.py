from aoc2023.day20.day20_common import PulsePropagation


def main():
    pp = PulsePropagation()

    while pp.button_presses < 1000:
        pp.push_button()

    print(pp.score)


if __name__ == '__main__':
    main()
