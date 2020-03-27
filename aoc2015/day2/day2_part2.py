from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    total = 0
    for line in f:
        dimensions = map(int, line.split("x"))
        dimensions.sort()
        total += 2*dimensions[0] + 2*dimensions[1] + (dimensions[0]*dimensions[1]*dimensions[2])

print(total)
