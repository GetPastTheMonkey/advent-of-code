from utils import get_input, chunk


def main():
    valid_triangles = 0

    with get_input(__file__) as f:
        for line in map(lambda x: x.rstrip(), f):
            sides = list(map(int, chunk(line, 5)))
            sides.sort()

            if sides[0] + sides[1] > sides[2]:
                valid_triangles += 1

    print(valid_triangles)


if __name__ == '__main__':
    main()
