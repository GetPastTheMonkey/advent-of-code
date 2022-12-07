from aoc2022.day7.day7_common import build_fs


def main():
    fs = build_fs()

    capacity = 70000000
    required = 30000000

    free = capacity - fs.size
    needed = required - free

    print(min(filter(lambda x: x > needed, fs.get_sizes_as_list())))


if __name__ == '__main__':
    main()
