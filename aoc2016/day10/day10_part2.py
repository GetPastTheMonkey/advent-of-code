from aoc2016.day10.day10_common import run_network


def main():
    outputs, _ = run_network()
    print(outputs[0] * outputs[1] * outputs[2])


if __name__ == '__main__':
    main()
