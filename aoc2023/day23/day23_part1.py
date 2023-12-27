from queue import Queue

from aoc2023.day23.day23_common import day23_parse_grid, Vector

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}  # type: dict[str, Vector]


def main():
    grid = day23_parse_grid()
    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)
    first_step = (1, start[1])

    queue = Queue()  # type: Queue[tuple[Vector, set[Vector]]]
    queue.put((first_step, {start, first_step}))

    max_path = None  # type: int | None

    while not queue.empty():
        pos, visited = queue.get()

        if pos == end:
            path_len = len(visited) - 1
            max_path = path_len if max_path is None else max(max_path, path_len)
            continue

        for direction in DIRECTIONS.values():
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            char = grid[new_pos[0]][new_pos[1]]

            if new_pos in visited or char == "#":
                # Either already visited this square, or square is a forest tile
                continue

            newly_visited = {new_pos}  # type: set[Vector]

            if char != ".":
                # Char is an arrow
                direction = DIRECTIONS[char]
                new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
                newly_visited.add(new_pos)

                if new_pos in visited:
                    # Cannot take this arrow as it will bring me to an already visited tile
                    continue

            queue.put((new_pos, visited | newly_visited))

    print(max_path)


if __name__ == '__main__':
    main()
