from aoc2024.day12.day12_common import get_areas


def get_box(area: set[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x = max_x = min_y = max_y = None

    for x, y in area:
        min_x = x if min_x is None else min(min_x, x)
        max_x = x if max_x is None else max(max_x, x)
        min_y = y if min_y is None else min(min_y, y)
        max_y = y if max_y is None else max(max_y, y)

    return min_x, max_x, min_y, max_y


def main():
    s = 0

    for area, _ in get_areas():
        min_x, max_x, min_y, max_y = get_box(area)
        corners = 0

        for x in range(min_x - 1, max_x + 1):
            for y in range(min_y - 1, max_y + 1):
                top_left = (x, y) in area
                top_right = (x, y + 1) in area
                bot_left = (x + 1, y) in area
                bot_right = (x + 1, y + 1) in area
                num_true = sum(1 for c in [top_left, top_right, bot_left, bot_right] if c)

                if num_true == 1 or num_true == 3:
                    corners += 1
                elif top_left and not top_right and not bot_left and bot_right:
                    corners += 2
                elif not top_left and top_right and bot_left and not bot_right:
                    corners += 2

        s += len(area) * corners

    print(s)


if __name__ == '__main__':
    main()
