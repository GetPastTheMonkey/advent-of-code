from aoc2022.day7.day7_common import build_fs


def main():
    fs = build_fs()
    print(sum(filter(lambda x: x <= 100000, fs.get_sizes_as_list())))


if __name__ == '__main__':
    main()
