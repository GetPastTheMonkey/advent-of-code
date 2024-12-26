from aoc2024.day18.day18_common import day18_input, day18_shortest_path


def main():
    all_coords = day18_input()

    if len(all_coords) > 1000:
        num_coords = 1024
        end = 70
    else:
        num_coords = 12
        end = 6

    coords = set(all_coords[:num_coords])
    path = day18_shortest_path(coords, end)
    print(len(path))


if __name__ == '__main__':
    main()
