from aoc2022.day22.day22_common import load_data, DIRECTIONS, OPEN, WALL, VOID


def walk():
    grid, position, movement = load_data()
    direction = 0

    for moves, turn in movement:
        # Move as long as possible in this direction
        for _ in range(moves):
            new_row = position[0] + DIRECTIONS[direction][0]
            new_col = position[1] + DIRECTIONS[direction][1]

            try:
                new_tile = grid[new_row][new_col]

                if new_tile == OPEN:
                    position = new_row, new_col
                    continue
                elif new_tile == WALL:
                    break
                elif new_tile != VOID:
                    raise ValueError(f"Unknown grid tile state: {new_tile}")
            except IndexError:
                pass

            # If program reaches this point, either stepped off grid or stepped into void
            while True:
                new_row = (new_row - DIRECTIONS[direction][0])
                new_col = (new_col - DIRECTIONS[direction][1])

                if not (0 <= new_row < len(grid)):
                    break

                if not (0 <= new_col < len(grid[0])):
                    break

                if grid[new_row][new_col] == VOID:
                    break

            new_row += DIRECTIONS[direction][0]
            new_col += DIRECTIONS[direction][1]

            if grid[new_row][new_col] == WALL:
                break
            elif grid[new_row][new_col] == OPEN:
                position = new_row, new_col
            else:
                raise ValueError("Flow error!")

        # Turn into given direction
        if turn is None:
            pass
        elif turn == "L":
            direction = (direction - 1) % len(DIRECTIONS)
        elif turn == "R":
            direction = (direction + 1) % len(DIRECTIONS)
        else:
            raise ValueError(f"Unknown turn signal: {turn}")

    return position[0], position[1], direction


def main():
    row, col, direction = walk()
    print(sum([1000 * (row + 1), 4 * (col + 1), direction]))


if __name__ == '__main__':
    main()
