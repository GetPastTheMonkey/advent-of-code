from utils import get_input_lines


def day9_input():
    line = next(get_input_lines(__file__))
    block_id = 0
    layout = []
    none_count = 0

    for count, num in enumerate(line):
        if count % 2 == 0:
            for _ in range(int(num)):
                layout.append(block_id)

            block_id += 1
        else:
            for _ in range(int(num)):
                layout.append(None)

            none_count += int(num)

    return layout, none_count


def compress(layout: list[int | None], none_count: int):
    idx = 0

    while none_count:
        block_id = layout.pop()

        if block_id is not None:
            while layout[idx] is not None:
                idx += 1

            layout[idx] = block_id

        none_count -= 1

    return layout


def checksum(layout: list[int]) -> int:
    s = 0

    for idx, file_id in enumerate(layout):
        s += idx * file_id

    return s


def main():
    print(checksum(compress(*day9_input())))


if __name__ == '__main__':
    main()
