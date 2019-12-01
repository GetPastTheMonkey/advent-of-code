from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    print(sum([((int(x) // 3) - 2) for x in f]))
