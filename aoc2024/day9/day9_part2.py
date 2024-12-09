from utils import get_input_lines


def day9_input():
    line = next(get_input_lines(__file__))

    block_start = 0
    block_id = 0

    # Files: (block_start, block_size, block_id)
    files = []  # type: list[tuple[int, int, int]]

    # Gaps: (block_start, block_size)
    gaps = []  # type: list[tuple[int, int]]

    for count, num in enumerate(map(int, line)):
        if count % 2 == 0:
            files.append((block_start, num, block_id))
            block_id += 1
        else:
            gaps.append((block_start, num))

        block_start += num

    return files, gaps


def main():
    files, gaps = day9_input()
    s = 0

    for file_start, file_size, file_id in reversed(files):
        for gap_idx in range(len(gaps)):
            gap_start, gap_size = gaps[gap_idx]

            if gap_start > file_start:
                break

            if gap_size >= file_size:
                gaps[gap_idx] = (gap_start + file_size, gap_size - file_size)
                file_start = gap_start
                break

        s += sum(file_start + i for i in range(file_size)) * file_id

    print(s)


if __name__ == '__main__':
    main()
