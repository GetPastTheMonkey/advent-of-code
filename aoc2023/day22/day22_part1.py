from aoc2023.day22.day22_common import get_dependencies


def main():
    dependencies = get_dependencies()
    non_removable = {list(deps)[0] for deps in dependencies if len(deps) == 1}
    print(len(dependencies) - len(non_removable))


if __name__ == '__main__':
    main()
