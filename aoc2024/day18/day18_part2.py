from aoc2024.day18.day18_common import day18_input, day18_shortest_path


def main():
    all_coords = day18_input()
    end = 70 if len(all_coords) > 1000 else 6

    current_coords = set()
    current_path = day18_shortest_path(current_coords, end)

    for (x, y) in all_coords:
        current_coords.add((x, y))

        if (x, y) in current_path:
            current_path = day18_shortest_path(current_coords, end)

            if len(current_path) == 0:
                print(f"{x},{y}")


if __name__ == '__main__':
    main()
