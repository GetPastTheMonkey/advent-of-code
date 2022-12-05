from utils import get_input, chunk


def main():
    valid_triangles = 0

    with get_input(__file__) as f:
        for line_1, line_2, line_3 in chunk(list(map(lambda x: x.rstrip(), f)), 3):
            line_1_chunked = list(map(int, chunk(line_1, 5)))
            line_2_chunked = list(map(int, chunk(line_2, 5)))
            line_3_chunked = list(map(int, chunk(line_3, 5)))

            for i in range(3):
                triangle = [line_1_chunked[i], line_2_chunked[i], line_3_chunked[i]]
                triangle.sort()

                if triangle[0] + triangle[1] > triangle[2]:
                    valid_triangles += 1

    print(valid_triangles)


if __name__ == '__main__':
    main()
