from utils import get_input_lines


MAXIMUMS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main():
    s = 0

    for line in get_input_lines(__file__):
        game, draws = line.split(": ")

        game = int(game.split(" ")[1])
        possible = True

        for draw in draws.split("; "):
            for amount, color in map(lambda x: x.split(" "), draw.split(", ")):
                if color in MAXIMUMS and MAXIMUMS[color] < int(amount):
                    possible = False
                    break

            if not possible:
                break

        if possible:
            s += game

    print(s)


if __name__ == '__main__':
    main()
