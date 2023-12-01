from utils import get_input_lines


MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_first_digit(line: str) -> int:
    remainder = line

    while remainder:
        if remainder[0].isdigit():
            return int(remainder[0])

        for start, digit in MAPPING.items():
            if remainder.startswith(start):
                return digit

        remainder = remainder[1:]

    raise ValueError(f"Could not find a digit in string: {line}")


def find_last_digit(line: str) -> int:
    remainder = line

    while remainder:
        if remainder[-1].isdigit():
            return int(remainder[-1])

        for end, digit in MAPPING.items():
            if remainder.endswith(end):
                return digit

        remainder = remainder[:-1]

    raise ValueError(f"Could not find a digit in string: {line}")


def main():
    s = 0

    for line in get_input_lines(__file__):
        s += 10 * find_first_digit(line)
        s += find_last_digit(line)

    print(s)


if __name__ == '__main__':
    main()
