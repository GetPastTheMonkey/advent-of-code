from utils import get_input_lines

DIRECTIONS = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def is_touching(x, y):
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1


def sign(n):
    if n == 0:
        return 0
    if n > 0:
        return 1
    if n < 0:
        return -1


def day9_solve(snake_length):
    snake = [(0, 0)] * snake_length
    visited = set()
    visited.add(snake[-1])

    for line in get_input_lines(__file__):
        direction, length = line.split(" ")

        direction = DIRECTIONS[direction]
        length = int(length)

        for _ in range(length):
            snake[0] = snake[0][0] + direction[0], snake[0][1] + direction[1]

            for idx in range(1, snake_length):
                if not is_touching(snake[idx-1], snake[idx]):
                    head = snake[idx-1]
                    tail = snake[idx]

                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]

                    snake[idx] = tail[0] + sign(dx), tail[1] + sign(dy)

            visited.add(snake[-1])

    print(len(visited))
