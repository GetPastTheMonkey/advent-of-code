from os.path import join, dirname, realpath


def recursive_fuel(x):
    if x < 9:
        return 0
    new_fuel = (x // 3) - 2
    return new_fuel + recursive_fuel(new_fuel)


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    print(sum([recursive_fuel(int(x)) for x in f]))
