from utils import get_input_lines


def main():
    maximums = [0, 0, 0]
    current = 0
    for line in get_input_lines(__file__):
        if line:
            current += int(line)
        else:
            maximums[0] = max(maximums[0], current)
            maximums.sort()
            current = 0

    print(sum(maximums))


if __name__ == '__main__':
    main()
