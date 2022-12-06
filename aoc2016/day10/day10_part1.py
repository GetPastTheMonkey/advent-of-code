from aoc2016.day10.day10_common import run_network


def main():
    look_for = {17, 61}
    _, robots = run_network()

    for idx, bot in robots.items():
        if set(bot.get_values()) == look_for:
            print(idx)


if __name__ == '__main__':
    main()
