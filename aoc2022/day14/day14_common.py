from utils import get_input_lines


class Simulation:
    _EMPTY, _ROCK, _SAND = 0, 1, 2

    def __init__(self, part_1: bool):
        x_min = None
        x_max = None
        y_min = 0
        y_max = None

        x_groups = []
        y_groups = []

        for line in get_input_lines(__file__):
            coord_list = line.split(" -> ")

            for i in range(1, len(coord_list)):
                start = tuple(map(int, coord_list[i - 1].split(",")))
                end = tuple(map(int, coord_list[i].split(",")))

                if start[0] == end[0]:
                    y_start = min(start[1], end[1])
                    y_end = max(start[1], end[1])
                    x_groups.append((start[0], y_start, y_end))
                elif start[1] == end[1]:
                    x_start = min(start[0], end[0])
                    x_end = max(start[0], end[0])
                    y_groups.append((start[1], x_start, x_end))
                else:
                    raise ValueError(f"No matching coordinate")

                x_min = min(x_min, start[0], end[0]) if x_min is not None else min(start[0], end[0])
                x_max = max(x_max, start[0], end[0]) if x_max is not None else max(start[0], end[0])
                y_min = min(y_min, start[1], end[1]) if y_min is not None else min(start[1], end[1])
                y_max = max(y_max, start[1], end[1]) if y_max is not None else max(start[1], end[1])

        self._grid = []

        if not part_1:
            y_max += 2
            height = y_max - y_min + 1
            x_min -= height
            x_max += height
            y_groups.append((y_max, x_min, x_max))

        for y in range(y_max - y_min + 1):
            row = []
            for x in range(x_max - x_min + 1):
                row.append(self._EMPTY)
            self._grid.append(row)

        for x, y_start, y_end in x_groups:
            for y in range(y_start, y_end + 1):
                self._grid[y - y_min][x - x_min] = self._ROCK

        for y, x_start, x_end in y_groups:
            for x in range(x_start, x_end + 1):
                self._grid[y - y_min][x - x_min] = self._ROCK

        self._source = 500 - x_min, 0 - y_min
        self._count_sand = 0

    def _step(self) -> bool:
        x, y = self._source

        if self._grid[y][x] != self._EMPTY:
            # The source block is not empty, we should stop iterating
            return False

        while True:
            coords = [
                (x, y + 1),
                (x - 1, y + 1),
                (x + 1, y + 1)
            ]

            i = 0
            while i < len(coords):
                check_x, check_y = coords[i]
                try:
                    if self._grid[check_y][check_x] == self._EMPTY:
                        x, y = check_x, check_y
                        break
                except IndexError:
                    # The sand would flow out of the grid, we should stop iterating
                    return False

                i += 1

            if i == len(coords):
                # The sand did not flow down, we should let the sand rest and continue with the next iteration
                self._grid[y][x] = self._SAND
                self._count_sand += 1
                return True

    def run(self):
        should_continue = True

        while should_continue:
            should_continue = self._step()

        return self._count_sand
