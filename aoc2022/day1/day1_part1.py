from utils import get_input_lines


def main():
    maximum = 0
    current = 0
    for line in map(lambda x: x.strip(), get_input_lines(__file__)):
        if line:
            current += int(line)
        else:
            maximum = max(maximum, current)
            current = 0

    print(maximum)


if __name__ == '__main__':
    main()
