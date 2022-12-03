from utils import get_input_lines


def main():
    intersection_sum = 0

    for line in get_input_lines(__file__):
        assert len(line) % 2 == 0, "Line length not even"

        priorities = [ord(x) - ord("a") + 1 if x.islower() else ord(x) - ord("A") + 27 for x in line]
        half_a = set(priorities[:len(priorities) // 2])
        half_b = set(priorities[len(priorities) // 2:])

        intersection = half_a.intersection(half_b)
        assert len(intersection) == 1, "More than one element in both halves"
        intersection_sum += intersection.pop()

    print(intersection_sum)


if __name__ == '__main__':
    main()
